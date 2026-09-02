# Problems throughout

Floating Point - Found in tests
Floating point on def test_profit_calculator() was found to equal 6.4600000000001, :.2f formatting to decimal places hides this from view showing as 6.46.
pytest.approx(6.46) was added for the test version as it cannot be represented exactly in tests.

git rm --cached doesnt get rid of history. alreayd committed data can not be removed via this command. It stopped future commits to sales.csv from being tracked.
in this situation it meant nothing but iun the future it highlights the importance of .env being in the gitignore file as it include API Keys etc, on the first commit.

buy == 0 broke when items prices were entered as 0, as it was set to while buy == 0, meaning if they entered 0 it would just ask again as it was True.
So this was changed to While, try and break, where it must accept a float value even if thats 0.00.

Dictionaries use commas not semi-colons, incorrect syntax in python from other languages.

# Decisions

if __name__ == "__main__" guard Without it, importing the module runs the interactive loop, so the test file would start asking what I was selling.
The guard means the file behaves normally when run directly but exposes only its functions when imported. Testability depended on this.

Repeated input loops extracted into helpers The same validate-and-retry pattern appeared three times with only the prompt and the option list changing, 
so those became parameters. ask_from_list() and ask_for_price() reduced the main loop from around forty lines to six, and the validation logic now exists in one place. 
return inside the loop exits both the loop and the function, so no separate break is needed.

Append mode for the CSV, with a header check "a" appends; "w" would truncate the file on every run and destroy all previous records. newline="" prevents blank rows between entries on Windows.
Headers are written only when the file doesn't already exist, checked with os.path.exists(), which also makes the file self-recreating if deleted.

sales.csv in .gitignore, example_sales.csv committed The code should be public; my actual buy prices and sources shouldn't be. 
Committing a small example file means anyone cloning the repo can see the output format without seeing real data.

float not int for prices int("12.50") raises a ValueError. Prices have pence.