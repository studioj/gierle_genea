from datetime import datetime
import django
import os
from dbf import Table

test = Table("data/huwel.DBF")
i =0
test.open()
for record in test:
    i += 1
    print(record)
    if i == 10:
        break

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gierle_genea_web.settings")

django.setup()
from genea_viewer.models import Person


def parse_birthlist_to_persondata():
    i = 0
    person_list = []
    with open(file="data/birth_data/geboorte_exp2.txt") as birthfile:
        for line in birthfile.readlines():
            i += 1
            try:
                _, lastname, name, _, birth_date, _, _ = line.split("|")
                lastname = lastname.strip()
                name = name.strip()
                birth_date = birth_date.strip()
                if birth_date:
                    birth_date = datetime.strptime(birth_date, "%Y%m%d")
                    person_list.append(Person(name=lastname, first_name=name))

                # print(lastname, name, birth_date)
            except ValueError as v_error:
                if "not enough values to unpack (expected 7, got 1)" not in str(v_error):
                    raise
    return person_list


if __name__ == "__main__":
    Person.objects.all().delete()
    person_list = parse_birthlist_to_persondata()
    print(Person.objects.all().count())
    Person.objects.bulk_create(person_list)
    print(Person.objects.all().count())
    for lastname in ["Gevers", "Neefs", "Jacobs"]:
        geversens = Person.objects.all().filter(name=lastname)
        print(lastname, len(geversens))
        # for gevers in geversens:
        #     print(gevers.first_name)
