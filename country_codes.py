from pygal_maps_world import i18n


def get_country_code(country_name):
    # Return the pygal 2-digit country codes for the given country.

    for code, name in i18n.COUNTRIES.items():
        if name == country_name:
            return code
        """ if country_name == "Yemen":
            return "ye"
        elif country_name == "Bolivia, Plurinational State of":
            return "bo"
        elif country_name == "Venezuela, Bolivarian Republic of":
            return "bo"
        elif country_name == "Suriname":
            return "sr"
        elif country_name == "Tanzania, United Republic of":
            return "tz"
        elif country_name == "Congo, the Democratic Republic of the":
            return "cd"
        elif country_name == "Congo":
            return "cg"
        elif country_name == "Libyan Arab Jamahiriya":
            return "ly"
        elif country_name == "Egypt":
            return "eg"
        elif country_name == "Western Sahara":
            return "eh"
        elif country_name == "Iran, Islamic Republic of":
            return "ir"
        elif country_name == "Kyrgyzstan":
            return "kg"
        elif country_name == "Korea, Democratic People's Republic of":
            return "kp"
        elif country_name == "Korea, Republic of":
            return "kr"
        elif country_name == "Taiwan, Province of China":
            return "tw"
        elif country_name == "Lao People's Democratic Republic":
            return "la"
        elif country_name == "Viet Nam":
            return "vn" """

    # if the country code wasn't found, return none.
    return None


""" print(get_country_code("Andorra"))
print(get_country_code("United Arab Emirates"))
print(get_country_code("India"))
print(get_country_code("Russian Federation"))"""




