REM add an if statement to make a new folder called if_folder if one of the folders you created is named new_folder.
if exist "new_folder"(Folder new_folder exists. 
			Create a new folder called "if_folder"
    			 mkdir if_folder)


:: add an if-else statement that makes a new folder called hyperionDev if an if_folder exists,or else make a new folder called new-projects if it does not.

REM Check if the folder "if_folder" exists
if exist "if_folder" (
    REM Folder "if_folder" exists.
    REM Create a new folder called "hyperionDev"
    mkdir hyperionDev)
  else (
    REM Folder "hyperionDev" does not exist.
    REM Create a new folder called "new-projects"
    mkdir new-projects)

