import requests

from datatypes import VenueSlot
from datetime import datetime

from reservation import ReservationDetails

class AvailableSlot:

    def __init__(self, data: VenueSlot, seat_count: int):
        self.table_id = data["table"]["id"]

        self.config_id = data["config"]["id"]
        self.config_token = data["config"]["token"]
        self.config = data["config"]["type"]

        self.start_time = datetime.strptime(data["date"]["start"], "%Y-%m-%d %H:%M:%S")
        self.end_time = datetime.strptime(data["date"]["end"], "%Y-%m-%d %H:%M:%S")

        self.payment_info = data["payment"]

        self.seat_count = seat_count

    def print_payment_info(self):

        payment = self.payment_info

        print(f'Reservation Fee: {payment["deposit_fee"]} Per Guest')
        if payment["cancellation_fee"] is None:
            print(f'Reservation Cancellation Fee: $0.00')
        else:
            print(f'Reservation Cancellation Fee: {payment["cancellation_fee"]}')
        print(f"Venue share of the fee: {payment['venue_share']}%")

    def post(self, url: str, payload: dict, headers: dict):
        try:
            resp = requests.post(url, json=payload, headers=headers)
            if not resp.ok:
                resp.raise_for_status()

            data = resp.json()
        except requests.RequestException as e:
            print("Could not get Reservation details")
            return
        except requests.JSONDecodeError as e:
            print("Could not get Reservation details")
            return
        else:
            return data

    @staticmethod
    def print_reservation_details(data: ReservationDetails):

    def get_reservation_details(self, commit=0):
        url = "https://api.resy.com/3/details"

        payload = {
            "commit": commit,
            "config_id": self.config_id,
            "day": self.start_time.strftime("%Y-%m-%d"),
            "party_size": self.seat_count
        }

        headers = {
            "accept": "application/json, text/plain, */*",
            "accept-language": "en-US,en;q=0.9,es-419;q=0.8,es;q=0.7,pt;q=0.6,fr;q=0.5",
            "authorization": "ResyAPI api_key=\"VbWk7s3L4KiK5fzlO7JD3Q5EYolJI7n5\"",
            "cache-control": "no-cache",
            "content-type": "application/json",
            "pragma": "no-cache",
            "sec-ch-ua": "\"Chromium\";v=\"122\", \"Not(A:Brand\";v=\"24\", \"Google Chrome\";v=\"122\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Linux\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "x-origin": "https://widgets.resy.com",
            "Referer": "https://widgets.resy.com/",
            "Referrer-Policy": "strict-origin-when-cross-origin",
        }

        data: ReservationDetails | None = self.post(url, payload, headers)

        if data is None:
            return
        else:
            self.print_reservation_details()



