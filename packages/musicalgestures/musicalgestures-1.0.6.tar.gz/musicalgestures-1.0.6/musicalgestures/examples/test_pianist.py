import musicalgestures

# CREATE MODULE OBJECT: Here is an example call to create an mg Object, using loads of parameters
mg = musicalgestures.MgObject('pianist.avi', color=False, crop='auto', skip=3)
# USE MODULE METHOD: To run the motionvideo analysis, run the function using your object,
# then create the motion history by chaining the history() function onto the result of the previous (motion) function
mg.motion(inverted_motionvideo=True, inverted_motiongram=True,
          thresh=0.1, blur='Average').history(history_length=25)

# Average image of original video
# mg.average('pianist.avi')

# Average image of pre-processed video
mg.average()

# Average image of motion video
mg.average(mg.of+'_motion.avi')
