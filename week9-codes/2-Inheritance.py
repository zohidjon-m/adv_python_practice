
# #############################################Inheritance without __init__
# class FootBall:
#     def __init__(self, country, division, no_of_times):
#         self.country = country
#         self.division = division
#         self.no_of_times = no_of_times
#     def fifa(self):
#         print(f"{self.country} team plays in {self.division} division.")

# class WorldChampions(FootBall):
#     def world_championship(self):
#         print(f"{self.country} team has won {self.no_of_times} times!")
# germany = WorldChampions("Germany", "UEFA", 4)
# germany.fifa()
# germany.world_championship()
# #############################################
# # 1. The 'Country' class is the parent (base) class.
# # 2. The 'HappiestCountry' class is the child (derived) class.
# # 3. 'super()' is used to call the parent class __init__() 
# #    so we don’t repeat code.
# # 4. The child class can add new attributes or methods while 
# #    keeping everything from the parent.

# ===============================
# Parent Class: Country
# ===============================
class Country:
    def __init__(self, country_name, population):
        self.country_name = country_name
        self.population = population

    def show_details(self):
        print(f"Country: {self.country_name}, Population: {self.population}")


# # ===============================
# # Child Class: HappiestCountry
# # ===============================
class HappiestCountry(Country):
    def __init__(self, country_name, population, continent, happiness_rank):
        # Call the parent class constructor
        super().__init__(country_name, population)

        # New attributes for subclass
        self.continent = continent
        self.happiness_rank = happiness_rank

    # Override parent method and reuse it using super()
    def show_details(self):
        super().show_details()  # Call parent’s version
        print(f"Continent: {self.continent}, Happiness Rank: {self.happiness_rank}")


# Create object of subclass
finland = HappiestCountry("Finland", 5_563_000, "Europe", 1)

# Show detailed information
finland.show_details()

