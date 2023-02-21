# Python-CLI
Layout to make an easy CLI in python.

Just add to bin/ any command you want to be able to execute. You can sort them into folders if you wish.

For instance, you can have a folder `bin/select/`, on which commands `car.py`, `house.py` and `street.py` are. Then, each of them might be called as `select car [arguments]`, or `select house [arguments]`.

Keep in mind that if you wish to have access to such arguments, your command module (`car.py`, for example) should have a function called `main`, `run`, `execute`, or exactly as your command's basename. This function will be called exactly after importing it. Also remember that if two of these functions are found in a single file, only one of them will be called (probably the first one that was defined), so avoid using these names for functions except for when you want them to be called by the CLI.
