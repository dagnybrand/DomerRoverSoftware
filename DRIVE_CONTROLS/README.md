*before driving, verify IP address using* ping raspberrypi.local *on home computer. ensure "host" in every program is the IP address of the pi*

**TO DRIVE THE ROVER**
1. run "python3 server.py" in pi terminal
2. run "python3 client2.py" in computer terminal
3. press 1234 for controls, hold to send continuously
4. press ESC to exit

**TO STREAM VIDEO FEED**
1. run "python3 stream_server_2.py" in pi terminal
2. run "python3 video_client.py" in computer terminal
3. video feed appears on computer

*THESE PROGRAMS CAN BE RUN SIMULTANIOUSLY -- JUST OPEN TWO TERMINALS*

*a "messaging" program is in progress, will be able to run at the same time as other two and allow the rover to send messages to the computer"