# Python-CLI
Very simple automatic CLI for python.

Just add to bin/ any command you want to be able to execute. You can sort them into folders if you wish.

For instance, you can have a folder `bin/select/`, on which commands `car.py`, `house.py` and `street.py` are. Then, each of them might be called as `select car [arguments]`, or `select house [arguments]`.

Keep in mind that if you wish to have access to such arguments, your command module (`car.py`, for example) should have a function called `main`, `run`, `execute`, or exactly as your command's basename. This function can have an arguments parameter, which will give you a list of strings passed by the user.

The main function of each command will be called exactly after importing it. Also remember that if two of these main functions are found in a single file, only one of them will be called (probably the first one that was defined), so avoid using `main`, `run`... for naming functions except for when you want them to be called by the CLI.
