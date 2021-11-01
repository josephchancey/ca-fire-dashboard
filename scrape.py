# Import dependencies


def scrapeData():
    import urllib.request, json 
    from bson.json_util import dumps, loads
    import os, ssl
    import pymongo
    import itertools
    import pandas as pd


    # ### 2021

    if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
    getattr(ssl, '_create_unverified_context', None)):
        ssl._create_default_https_context = ssl._create_unverified_context

    with urllib.request.urlopen("https://www.fire.ca.gov/umbraco/api/IncidentApi/List?inactive=true&year=2021") as url:
        inactive_2021 = json.loads(url.read().decode())
        # print(json.dumps(data, indent=4, sort_keys=False))

    with urllib.request.urlopen("https://www.fire.ca.gov/umbraco/api/IncidentApi/List?inactive=false&year=2021") as url:
        active_2021 = json.loads(url.read().decode())

        # print(json.dumps(data, indent=4, sort_keys=False))


    # ## 2020

    with urllib.request.urlopen("https://www.fire.ca.gov/umbraco/api/IncidentApi/List?inactive=true&year=2020") as url:
        inactive_2020 = json.loads(url.read().decode())
        # print(json.dumps(data, indent=4, sort_keys=False))

    with urllib.request.urlopen("https://www.fire.ca.gov/umbraco/api/IncidentApi/List?inactive=false&year=2020") as url:
        active_2020 = json.loads(url.read().decode())
        # print(json.dumps(data, indent=4, sort_keys=False))


    # ## 2019

    with urllib.request.urlopen("https://www.fire.ca.gov/umbraco/api/IncidentApi/List?inactive=true&year=2019") as url:
        inactive_2019 = json.loads(url.read().decode())
        # print(json.dumps(data, indent=4, sort_keys=False))

    with urllib.request.urlopen("https://www.fire.ca.gov/umbraco/api/IncidentApi/List?inactive=false&year=2019") as url:
        active_2019 = json.loads(url.read().decode())


    # ## 2018

    with urllib.request.urlopen("https://www.fire.ca.gov/umbraco/api/IncidentApi/List?inactive=true&year=2018") as url:
        inactive_2018 = json.loads(url.read().decode())
        # print(json.dumps(data, indent=4, sort_keys=False))

    with urllib.request.urlopen("https://www.fire.ca.gov/umbraco/api/IncidentApi/List?inactive=false&year=2018") as url:
        active_2018 = json.loads(url.read().decode())
        # print(json.dumps(data, indent=4, sort_keys=False))


    # ## 2017

    with urllib.request.urlopen("https://www.fire.ca.gov/umbraco/api/IncidentApi/List?inactive=true&year=2017") as url:
        inactive_2017 = json.loads(url.read().decode())
        # print(json.dumps(data, indent=4, sort_keys=False))

    with urllib.request.urlopen("https://www.fire.ca.gov/umbraco/api/IncidentApi/List?inactive=false&year=2017") as url:
        active_2017 = json.loads(url.read().decode())
        # print(json.dumps(data, indent=4, sort_keys=False))


    # ## 2016

    with urllib.request.urlopen("https://www.fire.ca.gov/umbraco/api/IncidentApi/List?inactive=true&year=2016") as url:
        inactive_2016 = json.loads(url.read().decode())
        # print(json.dumps(data, indent=4, sort_keys=False))

    with urllib.request.urlopen("https://www.fire.ca.gov/umbraco/api/IncidentApi/List?inactive=false&year=2016") as url:
        active_2016 = json.loads(url.read().decode())
        # print(json.dumps(data, indent=4, sort_keys=False))


    # ## 2015

    with urllib.request.urlopen("https://www.fire.ca.gov/umbraco/api/IncidentApi/List?inactive=true&year=2015") as url:
        inactive_2015 = json.loads(url.read().decode())
        # print(json.dumps(data, indent=4, sort_keys=False))

    with urllib.request.urlopen("https://www.fire.ca.gov/umbraco/api/IncidentApi/List?inactive=false&year=2015") as url:
        active_2015 = json.loads(url.read().decode())
        # print(json.dumps(data, indent=4, sort_keys=False))

    # ## 2014

    with urllib.request.urlopen("https://www.fire.ca.gov/umbraco/api/IncidentApi/List?inactive=true&year=2014") as url:
        inactive_2014 = json.loads(url.read().decode())
        # print(json.dumps(data, indent=4, sort_keys=False))

    with urllib.request.urlopen("https://www.fire.ca.gov/umbraco/api/IncidentApi/List?inactive=false&year=2014") as url:
        active_2014 = json.loads(url.read().decode())
        # print(json.dumps(data, indent=4, sort_keys=False))


    # ## 2013

    with urllib.request.urlopen("https://www.fire.ca.gov/umbraco/api/IncidentApi/List?inactive=true&year=2013") as url:
        inactive_2013 = json.loads(url.read().decode())
        # print(json.dumps(data, indent=4, sort_keys=False))

    with urllib.request.urlopen("https://www.fire.ca.gov/umbraco/api/IncidentApi/List?inactive=false&year=2013") as url:
        active_2013 = json.loads(url.read().decode())
        # print(json.dumps(data, indent=4, sort_keys=False))


    # ## Concat

    scraped_data = active_2021 + inactive_2021 + active_2020 + inactive_2020 + active_2019 + inactive_2019 + active_2018 + inactive_2018 + active_2017 + inactive_2017 + active_2016 + inactive_2016 + active_2015 + inactive_2015 + active_2014 + inactive_2014 + active_2013 + inactive_2013

    len(scraped_data)
    # scraped_data

    #delete all fire data with erroneus values for either Latitude or Longitude (values outside the range of possibility)
    final_data = []
    for item in scraped_data:
        if item["Latitude"] < 90 and item["Latitude"] > 0 and item["Longitude"] > -180 and item["Longitude"] < 180:
            final_data.append(item)
    # final_data

    final_df = pd.DataFrame(final_data)
    # print(min(final_df["Longitude"]))
    # print(max(final_df["Longitude"]))
    # print(min(final_df["Latitude"]))
    # print(max(final_df["Latitude"]))
    # fire_df


    # ## Pymongo

    # Initialize PyMongo to work with MongoDBs
    conn = 'mongodb://localhost:27017'
    client = pymongo.MongoClient(conn)

    # Define database and collection
    db = client.calfire
    collection = db.fires

    for item in final_data:
        collection.insert_one(item)

    #convert sq miles to total acreage in CA
    ca_area_miles = 163696
    ca_area_acreage = ca_area_miles * 640

    # # total_2021 = inactive_2021["AcresBurned"].sum()
    # final_data["Year"] = final_data["ExtinguishedDateOnly"].dt.year

    total_2021_burned = 0
    for fire in inactive_2021:
        try: 
            total_2021_burned += fire["AcresBurned"]
        except:
            continue
            
    for fire in active_2021:
        try: 
            total_2021_burned += fire["AcresBurned"]
        except:
            continue

    total_2020_burned = 0
    for fire in inactive_2020:
        try: 
            total_2020_burned += fire["AcresBurned"]
        except:
            continue
            
    for fire in active_2020:
        try: 
            total_2020_burned += fire["AcresBurned"]
        except:
            continue

    total_2019_burned = 0
    for fire in inactive_2019:
        try: 
            total_2019_burned += fire["AcresBurned"]
        except:
            continue
            
    for fire in active_2019:
        try: 
            total_2019_burned += fire["AcresBurned"]
        except:
            continue
            
    total_2018_burned = 0
    for fire in inactive_2018:
        try: 
            total_2018_burned += fire["AcresBurned"]
        except:
            continue
            
    for fire in active_2018:
        try: 
            total_2018_burned += fire["AcresBurned"]
        except:
            continue
            
    total_2017_burned = 0
    for fire in inactive_2017:
        try: 
            total_2017_burned += fire["AcresBurned"]
        except:
            continue
            
    for fire in active_2017:
        try: 
            total_2017_burned += fire["AcresBurned"]
        except:
            continue
            
    total_2016_burned = 0
    for fire in inactive_2016:
        try: 
            total_2016_burned += fire["AcresBurned"]
        except:
            continue
            
    for fire in active_2016:
        try: 
            total_2016_burned += fire["AcresBurned"]
        except:
            continue
            
    total_2015_burned = 0
    for fire in inactive_2015:
        try: 
            total_2015_burned += fire["AcresBurned"]
        except:
            continue
            
    for fire in active_2015:
        try: 
            total_2015_burned += fire["AcresBurned"]
        except:
            continue

    total_2014_burned = 0
    for fire in inactive_2014:
        try: 
            total_2014_burned += fire["AcresBurned"]
        except:
            continue
            
    for fire in active_2014:
        try: 
            total_2014_burned += fire["AcresBurned"]
        except:
            continue

    total_2013_burned = 0
    for fire in inactive_2013:
        try: 
            total_2013_burned += fire["AcresBurned"]
        except:
            continue
            
    for fire in active_2013:
        try: 
            total_2013_burned += fire["AcresBurned"]
        except:
            continue      
            
    # print(total_2021_burned, total_2020_burned, total_2019_burned, total_2018_burned,
    #       total_2017_burned,total_2016_burned,total_2015_burned, total_2014_burned,
    #      total_2013_burned)

    burned_by_year = pd.DataFrame({
        "2021 Recorded Burn Totals": [total_2021_burned],
        "2020 Recorded Burn Totals": [total_2020_burned],
        "2019 Recorded Burn Totals": [total_2019_burned],
        "2018 Recorded Burn Totals": [total_2018_burned],
        "2017 Recorded Burn Totals": [total_2017_burned],
        "2016 Recorded Burn Totals": [total_2016_burned],
        "2015 Recorded Burn Totals": [total_2015_burned],
        "2014 Recorded Burn Totals": [total_2014_burned],
        "2013 Recorded Burn Totals": [total_2013_burned],
        "2021 % of CA Burned": (total_2021_burned / ca_area_acreage) * 100,
        "2020 % of CA Burned": (total_2020_burned / ca_area_acreage) * 100,
        "2019 % of CA Burned": (total_2019_burned / ca_area_acreage) * 100,
        "2018 % of CA Burned": (total_2018_burned / ca_area_acreage) * 100,
        "2017 % of CA Burned": (total_2017_burned / ca_area_acreage) * 100,
        "2016 % of CA Burned": (total_2016_burned / ca_area_acreage) * 100,
        "2015 % of CA Burned": (total_2015_burned / ca_area_acreage) * 100,
        "2014 % of CA Burned": (total_2014_burned / ca_area_acreage) * 100,
        "2013 % of CA Burned": (total_2013_burned / ca_area_acreage) * 100,
    }, index = [0])

    burned_by_year_df = burned_by_year.transpose()
    burned_by_year_df.reset_index()
    burned_by_year_df = burned_by_year_df.rename(columns={0:"Acres Burned"})
    # burned_by_year_df

    # ca_burnt_since_2013 = total_2021_burned + total_2021_burned total_2021_burned +total_2021_burned +total_2021_burned +total_2021_burned +total_2021_burned +total_2021_burned +total_2021_burned +

    burned_by_year_df = pd.DataFrame(
        {"Year": ["2021", "2020", "2019", "2018", "2017", "2016", "2015", "2014",
                "2013"],
        
            "Total Recorded Burnt Acres":  [total_2021_burned, total_2020_burned, total_2019_burned,                                 total_2018_burned,total_2017_burned,total_2016_burned,total_2015_burned,
                                    total_2014_burned,total_2013_burned],
        "Total % of CA Burned" : [(total_2021_burned / ca_area_acreage) * 100,(total_2020_burned / ca_area_acreage) * 100,
                                (total_2019_burned / ca_area_acreage) * 100, (total_2018_burned / ca_area_acreage) * 100,
                                (total_2017_burned / ca_area_acreage) * 100, (total_2016_burned / ca_area_acreage) * 100,
                                (total_2015_burned / ca_area_acreage) * 100,(total_2014_burned / ca_area_acreage) * 100,
                                (total_2013_burned / ca_area_acreage) * 100,],
        "% of CA Burned Post 2013": [(total_2021_burned / ca_area_acreage) * 100 + (total_2020_burned / ca_area_acreage) * 100 +
                                (total_2019_burned / ca_area_acreage) * 100 + (total_2018_burned / ca_area_acreage) * 100 +
                                (total_2017_burned / ca_area_acreage) * 100 + (total_2016_burned / ca_area_acreage) * 100 +
                                (total_2015_burned / ca_area_acreage) * 100 + (total_2014_burned / ca_area_acreage) * 100 +
                                (total_2013_burned / ca_area_acreage) * 100,
                                    #2020
                                (total_2020_burned / ca_area_acreage) * 100 +
                                (total_2019_burned / ca_area_acreage) * 100 + (total_2018_burned / ca_area_acreage) * 100 +
                                (total_2017_burned / ca_area_acreage) * 100 + (total_2016_burned / ca_area_acreage) * 100 +
                                (total_2015_burned / ca_area_acreage) * 100 + (total_2014_burned / ca_area_acreage) * 100 +
                                (total_2013_burned / ca_area_acreage) * 100,
                                    #2019
                                (total_2019_burned / ca_area_acreage) * 100 + (total_2018_burned / ca_area_acreage) * 100 +
                                (total_2017_burned / ca_area_acreage) * 100 + (total_2016_burned / ca_area_acreage) * 100 +
                                (total_2015_burned / ca_area_acreage) * 100 + (total_2014_burned / ca_area_acreage) * 100 +
                                (total_2013_burned / ca_area_acreage) * 100, 
                                    #2018
                                (total_2018_burned / ca_area_acreage) * 100 +
                                (total_2017_burned / ca_area_acreage) * 100 + (total_2016_burned / ca_area_acreage) * 100 +
                                (total_2015_burned / ca_area_acreage) * 100 + (total_2014_burned / ca_area_acreage) * 100 +
                                (total_2013_burned / ca_area_acreage) * 100, 
                                    #2017
                                (total_2017_burned / ca_area_acreage) * 100 + (total_2016_burned / ca_area_acreage) * 100 +
                                (total_2015_burned / ca_area_acreage) * 100 + (total_2014_burned / ca_area_acreage) * 100 +
                                (total_2013_burned / ca_area_acreage) * 100, 
                                    #2016
                                    (total_2016_burned / ca_area_acreage) * 100 +
                                (total_2015_burned / ca_area_acreage) * 100 + (total_2014_burned / ca_area_acreage) * 100 +
                                (total_2013_burned / ca_area_acreage) * 100, 
                                    #2015
                                (total_2015_burned / ca_area_acreage) * 100 + (total_2014_burned / ca_area_acreage) * 100 +
                                (total_2013_burned / ca_area_acreage) * 100,
                                    #2014
                                (total_2014_burned / ca_area_acreage) * 100 +
                                (total_2013_burned / ca_area_acreage) * 100,
                                    #2013
                                    (total_2013_burned / ca_area_acreage)]
                        
                                
        })
 #   burned_by_year_df

    burned_by_year_df.to_csv("./burned_data.csv", index=False, header=True)

    print(burned_by_year_df)

    # Initialize PyMongo to work with MongoDBs

    # Define database and collection
    db = client.calfire

    converted_burned = pd.DataFrame.to_dict(burned_by_year_df, orient="records")
    converted_burned
    db.ca_burned.insert_many(converted_burned )

    return final_data, converted_burned 