# Mirror3D
Development code

3D_Track_8.py reads a detection input file (e.g., 3D_Track_FullStentor_5.csv), performs tracking by finding nearest object in previous frame and assign an ID to the output file (e.g., 3D_Track_FullStentor_6.csv). If the distance between the object in the current frame and the nearest matched object in the previous frame exceeds MAX_DISTANCE (set in the beginning of the code as a constant), a new ID is issued to the object. 
