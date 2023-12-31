# ytb

## Edit the program
Please change `path = ...` with the path where you want your files to be downloaded.

To use another audio format, please modify `.wav` by the format you'd like to use.

## Launch the program
Launch the program with python by typing `python ytb.py` in the program directory from the Terminal command line.

I personally use a shortcut with the short keyword `ytb` that launches the code from the right directory.

## How does it work ?
As you launch the program, you'll see the following interface in the Terminal command line. Enter the url of the desired video after "Video url:" then hit enter, and a red message will confirm that you successfully downloaded the wav file ! Go check your directory and you should immediately see the file.

<p align="center">
  <img src="img/download.png" width=70% height=70%>
</p>

## Use Terminal alias (mac)
Open or create the shell configuration file by typing `open ~/.zprofile` in the user’s home directory.

Add the line: `alias ytb='python /pathtofile/ytb.py'` with the right path to your file.

Now you can type `ytb` in the Terminal command line to launch the program.

## Libraries
This program uses pytube package.

## License
[MIT License](LICENSE)
