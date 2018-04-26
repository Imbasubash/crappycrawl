
import csv
import bs4
from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup


class Appfutura:

    # Defining the varialbes to be used
    def __init__(self, country):

        self.country = country

        self.page_number = []

        self.final_data = []

    # Setting up the url to be scraped & parsing
    def parser_page(self):
        pages=2
        for page in range(1, pages+1):

            home_page = "https://www.appfutura.com/app-developers/{}?p={}".format(
                self.country, page)
            uclient = ureq(home_page)
            page_html = uclient.read()
            uclient.close()

            # parsing the desire content
            page_soup = soup(page_html, "html.parser")
            self.page_number .append(page_soup)

    # Data_extraction
    def data_scrapper(self):

        for parsed_page in self.page_number:

            page_index = parsed_page

            developers = page_index.findAll("li", {"class": "widget"})

            # Extracting part
            for app_dev in developers:

                # developer name
                app_dev_name = app_dev.h3.text

                print("deve_name" "=" + app_dev_name)

            # Employee Details and budget
                number_of_employee = "data not avilable "

                project_value = "data not avilable"

                employee_node = app_dev.find("ul")

                if employee_node is not None:
                    employee_project = employee_node.findAll("li")

                    employee_count = len(employee_project)

                    if employee_count == 2:
                        number_of_employee = employee_project[0].text

                        project_value = employee_project[1].text

                        print(number_of_employee + "\n" + project_value)

                else:

                    print("employee and project data =" +
                          number_of_employee + "\n" + project_value)

                # WebSite
                web_site = app_dev.find("a").get("href")

                print("web_site  = " + web_site)

            # Founded Year&HourPay
                developer_page = web_site
                uclient = ureq(developer_page)
                page_html = uclient.read()
                uclient.close()

                cpage = soup(page_html, "html.parser")
                master_data = cpage.find("ul", {"class": "list-inline no-mar"})

                founded_year = "data not avaliable"

                founded_year_node = master_data.find(
                    "span", {"itemprop": "foundingDate"})

                if founded_year_node is not None:
                   founded_year = founded_year_node.text

                print("Founded in " +founded_year)

                # HourPay

                hourpay = "data not avaliable"
                salary = master_data.findAll("li")
                count = len(salary)

                if count == 6:
                    hourpay = salary[5].text
                    print(hourpay)

            # Ratings&Review

                ratings_reviews = app_dev.find(
                    "div", {"class": "inline-block"})

                rate_review = ratings_reviews.findAll("span")

                ratings = rate_review[0].text

                reviews = rate_review[1].text

                print(ratings + "\n" + reviews)

                # Appending the data to list
                dic_data = {'app_dev_name': app_dev_name, 'employeemployee_count': number_of_employee, 'project budge': project_value,
                            "web_site": web_site, 'f_year':founded_year, 'Hourpay': hourpay, 'val': ratings, 'val1': reviews}

                self.final_data.append(dic_data)

    
    # CSV Writer:
    def csv_writer(self, filename):

        self.filename = filename

        with open(self.filename, "w") as f:

            headers = "App dev Name,Empno,networth,web_sites,Founded In,HourPay,Rating,Review\n"

            f.write(headers)

            w = csv.writer(f)

            for data in self.final_data:

                data_writer = data.values()

                w.writerow(data_writer)


contries = ["australia", "canada", "germany", "india",
            "poland", "united-kingdom", "united-states"]


for country in contries:
   
    Bs = Appfutura(country)
    
    Bs.parser_page()

    Bs.data_scrapper()

    Bs.csv_writer("Top Appdevlopers in {} AppDev.csv".format(country))

# end of the program
