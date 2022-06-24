import pandas as pd

def OneParameterGreaterThan():
    print("---------------------------------------------------------------------------------")
    global Turn_File_Into_Dataframe  # makes it a global var to be used within definitions
    global Ask_For_File_Path

    Count_Dataframe_Rows = 0

    with open(Ask_For_File_Path) as file:  # Use file to refer to the file
        for i in file:
            Count_Dataframe_Rows = Count_Dataframe_Rows + int(1)

    print("There are", Count_Dataframe_Rows, "rows counted in this Dataframe")

    User_Entered_Parameter_Greater = input("What number do you want to enter as your parameter? Remember, the created "
                                           "Dataframe will only display "
                                           "rows of data with values greater than thisIt can be an INT or a FLOAT: ")  # the parameter to search by

    print(Turn_File_Into_Dataframe.columns)  # prints current column names

    Column_User_Selects_To_Search = input("Which column do you want to search by? Column names are listed above and "
                                          "are case sensitive, copy and "
                                          "past everything within the ' ' of your chosen column, including a space: ")

    User_Selected_Column = Turn_File_Into_Dataframe[
        Column_User_Selects_To_Search]  # Column_User_Selects_To_Search var is passed into popPop to be iterated over later in line 21 and 26

    Take_First_Dataframe_Column = Turn_File_Into_Dataframe.iloc[:,
                                  0]  # automatically takes the first column of the Data_Frame which is needed for line 21

    indx = []

    for x in range(
            len(Take_First_Dataframe_Column)):  # for some x in the range of the length of the var named Take_First_Dataframe_Column
        if float(User_Entered_Parameter_Greater) > User_Selected_Column[x]:
            indx.append(x)

    Data_Frame = pd.DataFrame()

    for indexes in indx:
        Data_Frame = Data_Frame.append(Turn_File_Into_Dataframe.iloc[indexes])

    Data_Frame = Turn_File_Into_Dataframe.where(User_Selected_Column > float(User_Entered_Parameter_Greater))

    Drop_All_Na_From_Dataframe = Data_Frame.dropna()

    print(Drop_All_Na_From_Dataframe.to_string())

    Ask_User_To_Save_Dataframe = input("Do you want to save your Dataframe, above, as a file to this computer? Yes or "
                                       "No: ")

    if Ask_User_To_Save_Dataframe == str("yes") or Ask_User_To_Save_Dataframe == str("Yes"):
        User_Names_Save_File = input("What do you want to name the file of the above Dataframe?: ")
        f = open(User_Names_Save_File, "x")
        Turn_Dataframe_To_String = Drop_All_Na_From_Dataframe.to_string()
        f.write(Turn_Dataframe_To_String)
        # f.close()

    elif Ask_User_To_Save_Dataframe == str("no") or Ask_User_To_Save_Dataframe == str("No"):
        print("Okay, The Dataframe above will NOT be saved to a file")
    print("---------------------------------------------------------------------------------")


def OneParameterLessThan():
    print("---------------------------------------------------------------------------------")
    global Turn_File_Into_Dataframe  # makes it a global var to be used within defininitions
    global Ask_For_File_Path

    Count_Dataframe_Rows = 0

    with open(Ask_For_File_Path) as file:  # Use file to refer to the file object
        for i in file:
            Count_Dataframe_Rows = Count_Dataframe_Rows + int(1)

    print("There are", Count_Dataframe_Rows, "rows in this dataframe")

    User_Entered_Parameter_Less = input("What number do you want to enter as your parameter? Remember, the created "
                                        "Dataframe will only display "
                                        "rows of data with values less than thisIt can be an INT or a FLOAT: ")  # the parameter to search by

    print(Turn_File_Into_Dataframe.columns)  # prints current column names

    Column_User_Selects_To_Search = input("Which column do you want to search by? Column names are listed aboue and "
                                          "are case sensitive, copy and past everything within the ' ' of your chosen"
                                          " column, including a space: ")

    User_Selected_Column = Turn_File_Into_Dataframe[
        Column_User_Selects_To_Search]  # Column_User_Selects_To_Search var is passed into popPop to be iterated over later in line 21 and 26

    Take_First_Dataframe_Column = Turn_File_Into_Dataframe.iloc[:,
                                  0]  # automatically takes the first column of the Data_Frame which is needed for line 21

    indx = []

    for x in range(
            len(Take_First_Dataframe_Column)):  # for some x in the range of the length of the var named Take_First_Dataframe_Column
        if float(User_Entered_Parameter_Less) < User_Selected_Column[x]:
            indx.append(x)

    Data_Frame = pd.DataFrame()

    for indexes in indx:
        Data_Frame = Data_Frame.append(Turn_File_Into_Dataframe.iloc[indexes])

    Data_Frame = Turn_File_Into_Dataframe.where(User_Selected_Column < float(User_Entered_Parameter_Less))

    Drop_All_Na_From_Dataframe = Data_Frame.dropna()

    print(Drop_All_Na_From_Dataframe.to_string())

    Ask_User_To_Save_Dataframe = input("Do you want to save your created Dataframe, as it is above, "
                                       "as a text file to your machine? Please enter 'yes' or 'no', it is case sen.: ")

    if Ask_User_To_Save_Dataframe == str("yes"):
        User_Names_Save_File = input("What do you want to name the text file of this created Dataframe?: ")
        f = open(User_Names_Save_File, "x")
        Turn_Dataframe_To_String = Drop_All_Na_From_Dataframe.to_string()
        f.write(Turn_Dataframe_To_String)
        f.close()

    elif Ask_User_To_Save_Dataframe == str("no") or Ask_User_To_Save_Dataframe == str("No"):
        print("Okay, The Dataframe above will NOT be saved to a file")

    print("---------------------------------------------------------------------------------")


def TwoParametersInbetween():
    print("---------------------------------------------------------------------------------")
    global Turn_File_Into_Dataframe  # makes it a global var to be used within defininitions
    global Ask_For_File_Path

    Count_Dataframe_Rows = 0

    with open(Ask_For_File_Path) as file:  # Use file to refer to the file object
        for i in file:
            Count_Dataframe_Rows = Count_Dataframe_Rows + int(1)

    print("There are", Count_Dataframe_Rows, "rows in this dataframe")

    User_Entered_Parameter_Min = input(
        "Enter a value to serve as the minimum parameter, remember the Dataframe will not return any rows with values "
        "less than this: ")

    User_Entered_Parameter_Max = input(
        "Enter a value to serve as the maximum parameter, remember the Dataframe will not return any rows with values "
        "greater than this: ")

    print(Turn_File_Into_Dataframe.columns)  # prints current column names

    Column_User_Selects_To_Search = input(
        "Which column do you want to search by? Column names are listed aboue and are case sensitive, copy and past "
        "everything within the ' ' of your chosen column, including a space: ")

    User_Selected_Column = Turn_File_Into_Dataframe[
        Column_User_Selects_To_Search]
    # Column_User_Selects_To_Search var is passed into popPop to be iterated over later in line 21 and 26

    Take_First_Dataframe_Column = Turn_File_Into_Dataframe.iloc[:,
                                  0]
    # automatically takes the first column of the Data_Frame which is needed for line 21

    indx = []

    for x in range(
            len(Take_First_Dataframe_Column)):
        # for some x in the range of the length of the var named Take_First_Dataframe_Column
        if float(User_Entered_Parameter_Min) < User_Selected_Column[x]:
            indx.append(x)

    Data_Frame = pd.DataFrame()

    for indexes in indx:
        Data_Frame = Data_Frame.append(Turn_File_Into_Dataframe.iloc[indexes])

    Data_Frame = Turn_File_Into_Dataframe.where(User_Selected_Column > float(User_Entered_Parameter_Min))

    Second_Dataframe_From_User_Minimum = Data_Frame[Column_User_Selects_To_Search]

    for x in range(
            len(Take_First_Dataframe_Column)):  # for some x in the range of the length of the var named Take_First_Dataframe_Column
        if float(User_Entered_Parameter_Max) > Second_Dataframe_From_User_Minimum[x]:
            indx.append(x)

    Final_Dataframe_From_User_Maximum = pd.DataFrame()

    for indexes in indx:
        Final_Dataframe_From_User_Maximum = Final_Dataframe_From_User_Maximum.append(Data_Frame.iloc[indexes])

    Final_Dataframe_From_User_Maximum = Turn_File_Into_Dataframe.where(
        Second_Dataframe_From_User_Minimum < float(User_Entered_Parameter_Max))

    Final_Dataframe_From_User_MaximumDropNa = Final_Dataframe_From_User_Maximum.dropna()

    print(Final_Dataframe_From_User_MaximumDropNa.to_string())

    Ask_User_To_Save_Dataframe = input("Do you want to save your created Dataframe, as it is above, "
                                       "as a text file to your machine? Please enter 'yes' or 'no', it is case sen.: ")

    if Ask_User_To_Save_Dataframe == str("yes"):
        User_Names_Save_File = input("What do you want to name the text file of this created Dataframe?: ")
        f = open(User_Names_Save_File, "x")
        Turn_Dataframe_To_String = Final_Dataframe_From_User_MaximumDropNa.to_string()
        f.write(Turn_Dataframe_To_String)
        f.close()

    elif Ask_User_To_Save_Dataframe == str("no") or Ask_User_To_Save_Dataframe == str("No"):
        print("Understandable")

    print("---------------------------------------------------------------------------------")


def main():
    import pandas as pd
    global Turn_File_Into_Dataframe
    global Delete_FirstRow

    Ask_User_How_Many_Parameter = input("How many parameters do you want to filter for, One or Two?: ")

    Ask_If_Parameter_Will_Be_Greater_Or_Less = input(
        "Do you want to filter for values Greater or Less THAN your given Parameter? Please only enter 'Less' or "
        "'Greater': ")

    Ask_For_File_Path = input(
        "Please enter the full file path of the File you want to turn into a Dataframe, when entering, "
        "leave off the ('') on the sides of the path else it will not be read correctly: ")

    if Ask_To_Delete_Line == str("Yes") or Ask_To_Delete_Line == str("yes"):
        with open(Ask_For_File_Path, 'r+') as f:  # open in read / write mode
            f.readline()  # read the first line and throw it out
            data = f.read()  # read the rest
            f.seek(0)  # set the cursor to the top of the file
            f.write(data)  # write the data back
            f.truncate()  # set the file size to the current size

    Turn_File_Into_Dataframe = pd.read_csv(Ask_For_File_Path, sep=",")

    if Ask_User_How_Many_Parameter == str("One") and Ask_If_Parameter_Will_Be_Greater_Or_Less == str("Greater"):
        OneParameterGreaterThan()
    elif Ask_User_How_Many_Parameter == str("One") and Ask_If_Parameter_Will_Be_Greater_Or_Less == str("Less"):
        OneParameterLessThan()
    elif Ask_User_How_Many_Parameter == str("Two"):
        TwoParametersInbetween()


Ask_User_How_Many_Parameter = input(
    "How many parameters do you want to filter for, 'One' or 'Two'?: ")  # Decides which function to use

Ask_If_Parameter_Will_Be_Greater_Or_Less = input("Do you want to filter for values Greater or Less THAN your given "
                                                 "Parameter? Please only enter 'Less' or 'Greater': ")

Ask_For_File_Path = input(
    "Please enter the full file path of the File you want to turn into a Dataframe, when entering, "
    "leave off the ('') on the sides of the path else it will not be read correctly: ")

Ask_To_Delete_Line = input("Do you need to delete the first line of the file? Only select this option if the first line"
                           "is anything other than the column headings. Yes or No?: ")

if Ask_To_Delete_Line == str("Yes") or Ask_To_Delete_Line == str("yes"):
    with open(Ask_For_File_Path, 'r+') as f:  # open in read / write mode
        f.readline()  # read the first line and throw it out
        data = f.read()  # read the rest
        f.seek(0)  # set the cursor to the top of the file
        f.write(data)  # write the data back
        f.truncate()  # set the file size to the current size

Turn_File_Into_Dataframe = pd.read_csv(Ask_For_File_Path, sep=",")

if Ask_User_How_Many_Parameter == str("One") and Ask_If_Parameter_Will_Be_Greater_Or_Less == str("Greater"):
    OneParameterGreaterThan()
elif Ask_User_How_Many_Parameter == str("One"
                                        " ") and Ask_If_Parameter_Will_Be_Greater_Or_Less == str("Less"):
    OneParameterLessThan()
elif Ask_User_How_Many_Parameter == str("Two"):
    TwoParametersInbetween()

askToRepeat = input(
    "Do you want to use this program once more? Yes or No:  ")  # decides if the program will run the main function

while askToRepeat == str("Yes"):
    main()
    askToRepeat = input("Do you want to use this program once more? Yes or No:  ")
else:
    print("Thank You")
