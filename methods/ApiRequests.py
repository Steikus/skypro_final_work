import requests


class ApiRequests:

    def __init__(self, url):
        self.url = url

    def registration_form(self, email: str):
        reg_form = {
            "email": email,
            "is_subscribe_agreed": False
            }
        my_headers = {
            'Content-Type': 'application/json;charset=utf-8',
        }
        resp = requests.post(self.url+'api/v3/site/accounts/v2/registration/', headers=my_headers, json=reg_form)
        return resp.json()

    def top_hotels_for_region(self, region: str):
        my_params = {
            "query": region
        }
        resp = requests.get(self.url+'api/site/multicomplete.json', params=my_params)
        return resp.json()

    def small_info_about_hotel(self, hotel_name: str):
        resp = requests.get(self.url+f'hotel/api/seo/v2/hotel/{hotel_name}/')
        return resp.json()['meta']['breadcrumbs'][-1]['link']

    def full_info_about_hotel(self, hotel_name: str):
        my_params = {
            'hotel': hotel_name
        }
        resp = requests.get(self.url+'hotel/search/v2/site/hp/content', params=my_params)
        return resp.json()

    def search_for_data(self, arrival_date: str, departure_date: str, region_id: int):
        hotel = {
            "session_params": {
                "search_uuid": "4cf5361b-b298-44e4-a8cf-6e49cddba885",
                "arrival_date": arrival_date,
                "departure_date": departure_date,
                "region_id": region_id,
                "paxes": [
                    {
                        "adults": 2
                    }
                ]
            }
        }
        session_id = {
            'session': '5dc3d6f6-9eaf-4622-8b83-a53582075b01'
        }
        resp = requests.post(self.url+'hotel/search/v2/site/serp', params=session_id, json=hotel)
        return resp.json()
