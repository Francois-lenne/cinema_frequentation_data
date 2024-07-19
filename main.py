from boxoffice_api import BoxOffice 


box_office = BoxOffice(api_key="a4735d63", outputformat="DF") # Get daily box office information for a specific date 


test_df = box_office.get_daily("2024-06-24")


print(test_df)
