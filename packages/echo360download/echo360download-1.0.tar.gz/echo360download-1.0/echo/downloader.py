from urllib.parse import urljoin

import dateutil
import requests
import json
import os
import shutil
import sys
import dateutil.parser as date_parser

from requests.utils import add_dict_to_cookiejar


class BaseURLSession(requests.Session):
    def __init__(self, prefix_url=None, *args, **kwargs):
        super(BaseURLSession, self).__init__(*args, **kwargs)
        self.prefix_url = prefix_url

    def request(self, method, url, *args, **kwargs):
        if not url.startswith(self.prefix_url):
            url = urljoin(self.prefix_url, url)
        return super(BaseURLSession, self).request(method, url, *args, **kwargs)


class EchoDownloader:
    def __init__(self, cookie_file='cookies.txt', debug_files=False, dest_directory='.'):
        self.debug_files = debug_files
        self.cookies = self.get_cookies(cookie_file)

        self.session = BaseURLSession(prefix_url="https://echo360.org.uk")
        add_dict_to_cookiejar(self.session.cookies, self.cookies)
        self.dest_directory = dest_directory


    def interactive(self):
        (courses, terms) = self.get_enrollments()
        for i, course in enumerate(courses):
            print(i, course['sectionName'])

        course_to_download = input(
            "\nEnter course indices you wish to download, separated by comma (empty or q to exit): ")
        if not course_to_download or course_to_download == 'q':
            return

        for c_id in map(int, course_to_download.split(',')):
            course = courses[c_id]
            courseTerm = terms[course["termId"]]["name"]

            self.download_course(courses[c_id], courseTerm)

    def get_cookies(self, cookie_file):
        cookies = {}
        with open(cookie_file, "r") as cFile:
            for ck in cFile:
                if not ck.strip() or ck.strip()[0] == "#":
                    continue
                cookieDomain = ck.strip().split("\t")[0]
                if "echo360.org.uk" not in cookieDomain:
                    continue
                try:
                    cookieName = ck.strip().split("\t")[5]
                    cookieData = ck.strip().split("\t")[6]
                    if cookieName == "PLAY_SESSION":
                        cookieData = cookieData.replace("&amp;", "&")
                    cookies[cookieName] = cookieData
                except:
                    pass  # stupid incorrectly-formatted data
        return cookies

    def get_enrollments(self):
        resp = self.session.get("/user/enrollments")
        resp.raise_for_status()

        if self.debug_files:
            with open("enrollment.json", "wb") as jf:
                jf.write(resp.text.encode("UTF-8"))

        try:
            jd = resp.json()
            courses = jd["data"][0]["userSections"]
            terms = jd["data"][0]["termsById"]
            return courses, terms
        except:
            raise SystemExit("Could not access signed-in Echo360."
                             "Make sure you have up-to-date cookies in 'cookies.txt'")

    def download_course(self, course, term_name):
        url = f"/section/{course['sectionId']}/syllabus"
        print(f"Downloading course: {course['courseCode']} ({course['courseName']})")

        resp = self.session.get(url)
        course_folder = os.path.join(term_name, course['courseCode'])
        json_file = os.path.join(course_folder, 'raw.json')
        os.makedirs(course_folder, exist_ok=True)

        if self.debug_files:
            with open(json_file, "wb") as jf:
                jf.write(resp.text.encode("UTF-8"))

        course_data = resp.json()["data"]
        self.download_lesson_list(course_data, course["courseName"], term_name)

    def download_lesson_list(self, lessonList, courseName, termName):
        for lesson in lessonList:
            if "groupInfo" in lesson:
                # this is not a lesson, but a group of lessons
                self.download_lesson_list(lesson["lessons"], courseName, termName)
            else:
                if lesson["lesson"]["hasAvailableVideo"]:
                    # time = lesson["lesson"]["lesson"]["timing"]["start"].replace(":",".")
                    try:
                        time = lesson["lesson"]["startTimeUTC"]
                    except:
                        time = lesson["lesson"]["lesson"]["createdAt"]
                    media = lesson["lesson"]["video"]["media"]["media"]["current"]
                    self.downloadHQ(media["primaryFiles"], time, "primary.mp4", courseName, termName)
                    if "secondaryFiles" in media and media["secondaryFiles"] != []:
                        self.downloadHQ(media["secondaryFiles"], time, "secondary.mp4", courseName, termName)
                if lesson["lesson"]["hasAvailableSlideDeck"]:
                    try:
                        time = lesson["lesson"]["startTimeUTC"]
                    except:
                        time = lesson["lesson"]["lesson"]["createdAt"]
                    slideDeck = lesson["lesson"]["slideDeck"]["media"]["media"]["originalFile"]
                    self.downloadResource(slideDeck["url"], time, slideDeck["name"], courseName, termName)

    def downloadHQ(self, medias, time, type, courseName, termName):
        bestIndex = 0
        for i in range(len(medias)):
            if medias[i]["size"] > medias[bestIndex]["size"]:
                bestIndex = i
        self.downloadResource(medias[bestIndex]["s3Url"], time, type, courseName, termName)

    def downloadResource(self, url, time, media_type, courseName, termName):
        dt = date_parser.parse(time)
        date_formatted = dt.strftime("%m.%d - %H%M")

        download_folder = os.path.join(self.dest_directory, termName, courseName)
        os.makedirs(download_folder, exist_ok=True)
        filename = f'{date_formatted} - {media_type}'
        filepath = os.path.join(download_folder, filename)

        if os.path.isfile(filepath):
            print("Keeping existing file: " + filepath)
            return

        print(f"Downloading resource: {filepath}")


        response = self.session.get(url, stream=True)
        if "html" in response.headers.get("content-type"):
            raise SystemExit(
                "A html file is where a binary file (video or slides) should be."
                "This probably means the cookies in 'cookies.txt' need updating."
            )
        with open(filepath, 'wb') as out_file:
            response.raw.decode_content = True
            shutil.copyfileobj(response.raw, out_file)
