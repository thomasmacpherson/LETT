
shape_index = [                     #      #
	       [              #     ##    ##    ###
	          # t-block  ###    #      #     #
		  [ [0,32,64,32],[-32,-32,-32,0] ],
	          [ [32,32,64,32],[-64,-32,-32,0] ],
	          [ [32,0,32,64],[-32,0,0,0] ],
	          [ [64,32,64,64],[-64,-32,-32,0] ]
	        ],
	        
	       [         
                                     ##
		  # square piece     ##      
	       	  [ [0,0,32,32],[0,-32,-32,0] ],
	       	  [ [0,0,32,32],[0,-32,-32,0] ],
	       	  [ [0,0,32,32],[0,-32,-32,0] ],
	       	  [ [0,0,32,32],[0,-32,-32,0] ],
	       ],
	       				#	##  	###	 #
		# rev- lblock		###	#	  #	 #
	       [       				#		##
	       	  [ [0,32,64,0],[-32,-32,-32,0] ],
	       	  [ [32,32,32,64],[-64,-32,0,0] ],
	       	  [ [64,0,32,64],[-32,0,0,0] ],
	       	  [ [0,32,32,32],[-64,-64,-32,0] ]
	       ],
	       		  	#	#	###	##
		#l block	###	#	#	 #
	       [			##		 #
	       	  [ [0,32,64,64],[-32,-32,-32,0] ],
	       	  [ [32,64,32,32],[-64,-64,-32,0] ],
	       	  [ [0,0,32,64],[-32,0,0,0] ],
	       	  [ [32,32,0,32],[-64,-32,0,0] ]
	       ],
	       				#	
		#rev zpiece	 ##	##			
	       [		##	 #		
	       	  [ [0,32,32,64],[-32,-32,0,0] ],
	       	  [ [32,0,32,0],[-64,-32,-32,0] ],
	       	  [ [0,32,32,64],[-32,-32,0,0] ],
	       	  [ [32,0,32,0],[-64,-32,-32,0] ] 
	       ],
				#		
				#
		#line piece	#	####		
	       [		#		
	       	  [ [0,32,64,96],[0,0,0,0] ],
	       	  [ [32,32,32,32],[-96,-64,-32,0] ],
	       	  [ [0,32,64,96],[0,0,0,0] ],
	       	  [ [32,32,32,32],[-96,-64,-32,0] ] 
	       ],
					 #      
		# z piece	##	##
	       [	 	 ##	#			
	       	  [ [32,64,0,32],[-32,-32,0,0] ],
	       	  [ [0,0,32,32],[-64,-32,-32,0] ],
	       	  [ [32,64,0,32],[-32,-32,0,0] ],
	       	  [ [0,0,32,32],[-64,-32,-32,0] ]
	       ]
	     ]


