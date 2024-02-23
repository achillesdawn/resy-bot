"""
This Python script is authored by Olivio (fiverr.com/olivo_).
Version: 1.0.0 (2024-02-24)
"""

import requests
import datetime

from time import sleep

from datatypes import VenueInfo, VenueData, VenueSlot, ScheduleData

from exceptions import TimeNotValid

from classes import AvailableSlot


class ReservationBot:
    venue_info: VenueInfo

    def __init__(
        self, desired_dates: list[str],
        start_time: str,
        end_time: str | None,
        num_seats: int = 4,
        venue_name: str = "ciccio-mio",
        location: str = "chi"
    ) -> None:

        today = datetime.date.today()
        self.START_DATE = today.strftime("%Y-%m-%d")
        one_year = today.replace(year=today.year + 1)
        self.END_DATE = one_year.strftime("%Y-%m-%d")

        self.DESIRED_DATES = desired_dates
        self.START_TIME = datetime.time.fromisoformat(start_time)
        self.END_TIME = datetime.time.fromisoformat(end_time)

        if self.START_TIME.hour >= self.END_TIME.hour:
            raise TimeNotValid("Start Time must be Earlier than End time by at least 1 hour")

        self.NUM_SEATS = num_seats
        self.VENUE_NAME = venue_name
        self.VENUE_LOCATION = location

        self.headers = {
            "accept": "application/json, text/plain, */*",
            "accept-language": "en-US,en;q=0.9,es-419;q=0.8,es;q=0.7,pt;q=0.6,fr;q=0.5",
            "authorization": 'ResyAPI api_key="VbWk7s3L4KiK5fzlO7JD3Q5EYolJI7n5"',
            "cache-control": "no-cache",
            "pragma": "no-cache",
            "sec-ch-ua": '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Linux"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "x-origin": "https://resy.com",
            "Referer": "https://resy.com/",
            "Referrer-Policy": "strict-origin-when-cross-origin",
        }

    def request_venue_info(self):
        url = f"https://api.resy.com/3/venue?url_slug={self.VENUE_NAME}&location={self.VENUE_LOCATION}"

        data: VenueData = self.get(url)

        self.print_venue(data)

        self.venue_info = VenueInfo(data["id"]["resy"], data["url_slug"], self.VENUE_LOCATION)

        print(self.venue_info)

    @staticmethod
    def print_venue(data: VenueData):
        print(f'[ {data["name"]} ]')
        print(f' ::{data["type"]}::')
        print("|", data["metadata"]["description"])

        for content in data["content"]:
            if content["name"] == "why_we_like_it":
                print("|", content["body"])

        print(
            "Rating", f'{data["rater"][0]["score"]:.2}/{data["rater"][0]["scale"]} |', data["rater"][0]["total"],
            "Rating"
        )
        print(data["contact"]["url"])
        print(data["large_party_message"])
        print("Min Party Size", data["min_party_size"])

    def get_url(self) -> str:
        return (
            f"https://api.resy.com/4/venue/calendar?venue_id={self.venue_info.id}"
            f"&num_seats={self.NUM_SEATS}"
            f"&start_date={self.START_DATE}"
            f"&end_date={self.END_DATE}"
        )

    def get(self, url: str) -> dict:

        total_retries = 3
        current_retry = 0
        for i in range(total_retries):
            try:
                response = requests.get(url, headers=self.headers)
            except requests.RequestException as e:

                if isinstance(e, requests.HTTPError):
                    print("Could not get resy.com, please check your internet connection")
                elif isinstance(e, requests.ConnectTimeout):
                    print("Connection Timed out. Please check your internet connection")
                elif isinstance(e, requests.ConnectionError):
                    print("Connection Error")
                else:
                    print("Could not get resy.com, please check your internet connection")

                if current_retry <= total_retries:
                    current_retry += 1
                    print("Retrying in 30 seconds")
                    sleep(30)
                    print(f"Retry #{current_retry}")
                    continue
                else:
                    raise e

            else:
                if not response.ok:
                    print("API returned status code", response.status_code, response.text)

                    if current_retry <= total_retries:
                        current_retry += 1
                        print("Retrying in 30 seconds")
                        sleep(30)
                        print(f"Retry #{current_retry}")
                        continue
                    else:
                        raise requests.RequestException

                else:
                    try:
                        data = response.json()
                    except requests.exceptions.JSONDecodeError as e:
                        raise e
                    else:
                        return data

    def execute(self):

        self.request_venue_info()

        url = self.get_url()
        print(url)

        try:
            data: ScheduleData = self.get(url)
        except (requests.RequestException, requests.JSONDecodeError):
            return

        available_dates = []
        for schedule in data["scheduled"]:
            if schedule["inventory"]["reservation"] != "sold-out":
                available_dates.append(schedule["date"])

        # Check if dates is desired date and times within start and end times
        for date in available_dates:
            url = (
                f"https://api.resy.com/4/find?lat=0&long=0"
                f"&day={date}"
                f"&party_size={self.NUM_SEATS}"
                f"&venue_id={self.venue_info.id}"
            )

            find = self.get(url)
            slots: list[VenueSlot] = find["results"]["venues"][0]["slots"]

            if len(slots) == 0:

            for slot in slots:
                slot = AvailableSlot(slot, seat_count=self.NUM_SEATS)
                if slot.is_within_time(self.START_TIME, self.END_TIME):
                    print(slot)



if __name__ == "__main__":
    r = ReservationBot(
        desired_dates=['2024-02-24', '2024-02-24'],
        start_time="19:00",
        end_time="21:00"
    )

    r.execute()
