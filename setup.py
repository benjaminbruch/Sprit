from cx_Freeze import setup, Executable

# Define the base for the executable. For macOS, we use None
base = None

# Define the executables
executables = [Executable("main.py", base=base, icon="files/app_icon.png")]

# Define the options for the build. Here we specify the packages to include, the path to the include files (like icons, database, etc.)
options = {
    "build_exe": {
        "packages": ["customtkinter", "sprit.view.stations_search_list_map_view"],
        "include_files": ["sprit/data/tk_hist.db", "sprit/resources/stations_icons", "sprit/resources/recommendation_icons"],
    }
}

# Call the setup function
setup(
    name="Sprit - Die Tankstellensuche",
    version="0.1",
    description="Finde die günstigste Tankstelle in deiner Nähe!",
    options=options,
    executables=executables
)