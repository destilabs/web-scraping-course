import requests

url = "https://www.udemy.com/api-2.0/pricing/?course_ids=1011712,1088256,1151632,1318112,1382702,1478886,1754098,2473048,2511476,2529790&fields[pricing_result]=price,discount_price,list_price,price_detail,price_serve_tracking_id"

payload={}
headers = {
  'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
  'X-Udemy-Cache-Release': '712d1df1acad8c5198d0',
  'X-Udemy-Cache-User': '59311329',
  'X-Udemy-Cache-Modern-Browser': '1',
  'X-Udemy-Cache-Language': 'en',
  'X-Udemy-Cache-Brand': 'UAen_US',
  'X-Requested-With': 'XMLHttpRequest',
  'X-Udemy-Cache-Logged-In': '1',
  'X-Udemy-Cache-Device': 'None',
  'sec-ch-ua-platform': '"Windows"',
  'sec-ch-ua-mobile': '?0',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36',
  'Accept': 'application/json, text/plain, */*',
  'X-Udemy-Cache-Version': '1',
  'X-Udemy-Cache-Price-Country': 'UA',
  'X-Udemy-Cache-Marketplace-Country': 'UA',
  'X-Udemy-Cache-Campaign-Code': 'LOYALR30222D',
  'Cookie': '__udmy_2_v57r=af2a56ea4c2c4712bb03fe8d9d38a75c; ud_firstvisit=2021-07-13T15:35:37.723902+00:00:1m3KRd:udNXWqEAomuKD0qpSNgbSdIh7O0; ud_rule_vars="eJyFjcsKwyAUBX8luG1TfCQ18VsEudFrKi2Vqskm5N8rabsunM2BGWYjBdKMBZ1ZQw4lJgWeQ39F6Cy3nWR8mqjwOLjRiQFkb5WN8R6QqIZsmjwgF1PiYm-mJPA-WJPjkiyaFVKA6YG6kprENMMzWE3O9fiQqnUEjYPyRTjlrKWyZaJhvRJ18iKZlJKdKFWUftwjmPC1YP4nD2MnRvqTd7K_AaBrSKI=:1m3KRd:We0pYWJ61cBwzjMdBP9S8jqBrOY"'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
