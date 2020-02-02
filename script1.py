from TestSim import TestSim


    
    # Get simulation ready to run.
s = TestSim();
   
    # Before we do anything, lets simulate the network off.
s.runTime(1);
   
    # Load the the layout of the network.
s.loadTopo("example.topo");

    # Add a noise model to all of the motes.
s.loadNoise("no_noise.txt");

    # Turn on all of the sensors.
s.bootAll();

    # Add the main channels. These channels are declared in includes/channels.h
s.addChannel(s.COMMAND_CHANNEL);
s.addChannel(s.GENERAL_CHANNEL);

    # After sending a ping, simulate a little to prevent collision.
s.runTime(1);
s.ping(1, 2, "Heck");
s.runTime(1);

s.ping(2, 3, "Hi!");
s.runTime(60);


