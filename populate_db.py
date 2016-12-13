#!/usr/bin/python
import xml.etree.ElementTree as etree
import urllib2
import datetime
import requests
from pollen_counts.quickstart.models import PollenCounts


def populate_db():
    pollen_xml = 'http://www.fmhdc.com/etc/PollenData/counts.xml'
    xml_doc = requests.get(pollen_xml).text
    root = etree.fromstring(xml_doc)
    pollen_dict = {}
    #root = tree.getroot()
    for pollendata in root:
        cur_date = "0000"
        for child in pollendata:
            print(child.tag,child.text)
            if child.tag == "date":
                pollen_dict[child.text] = {}
                cur_date = child.text
            else:
                pollen_dict[cur_date][child.tag] = child.text
    for date in pollen_dict:
        temp = PollenCounts()
        for key in pollen_dict[date]:
            cur_elem = pollen_dict[date][key]
            #print(key)
            if key == "time":
                date_elems = date.split('/')
                year = int(date_elems[2])
                month = int(date_elems[0])
                day = int(date_elems[1])
                time_elems = pollen_dict[date][key].split()
                hour_elems = time_elems[0].split(":")
                cur_min = int(hour_elems[1])
                cur_hour = int(hour_elems[0])
                print(cur_hour)
                if time_elems[1] == "PM" and cur_hour != 12:
                    cur_hour+=12
                temp_time = datetime.datetime(year,month,day,hour=cur_hour,minute=cur_min)
                temp.datetime = temp_time
            if key == "location":
                temp.location = cur_elem
            if key == "alder":
                temp.alder = float(cur_elem)
            if key == "willow":
                temp.willow = float(cur_elem)
            if key == "poplar_aspen":
                temp.poplar_aspen = float(cur_elem)
            if key == "birch":
                temp.birch = float(cur_elem)
            if key == "spruce":
                temp.spruce = float(cur_elem)
            if key == "other1_tree":
                temp.other1_tree = float(cur_elem)
            if key == "other2_tree":
                temp.other2_tree = float(cur_elem)
            if key == "grass":
                temp.grass = float(cur_elem)
            if key == "grass_2":
                temp.grass_2 = float(cur_elem)
            if key == "other1":
                temp.other1 = float(cur_elem)
            if key == "other2":
                temp.other2 = float(cur_elem)
            if key == "mold":
                temp.mold = float(cur_elem)
            if key == "total_pollen":
                temp.total_pollen = float(cur_elem)
            if key == "comments":
                temp.comments = str(cur_elem)
        temp.save()

