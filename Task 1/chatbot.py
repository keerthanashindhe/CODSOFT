def cooking_essential():
    print("Hi,How can I help you?")
    
    while True:
        user_input = input("You: ").upper()
        
        if user_input in["HI"]:
            print("cooking_essential: Hello!")
        
        elif user_input in["CAN YOU PROVIDE ME THE LIST OF ITEMS"]:
            print("cooking_essential:\nATTA & FLOUR\nRICE & POHA\nOIL & GHEE\nDRY FRUITS\nSALT,SUGAR & JAGGERY")
        
       
        elif user_input in["ATTA & FLOUR"]:
            print("cooking_essential:\nRAGI\nWHEAT\nBESAN\nMAIDA ")
        
        elif user_input in["RAGI"]:
            print("cooking_essential:\nRAGI\nRS48 FOR 1000g\nRS24 FOR 500g")
            
        elif user_input in["WHEAT"]:
            print("cooking_essential:\nWHEAT\nRS80 FOR 1000g\nRS40 FOR 500g")
            
        elif user_input in["BESAN"]:
            print("cooking_essential:\nBESAN\nRS50 FOR 1000g\nRS25 FOR 500g")
            
        elif user_input in["MAIDA"]:
            print("cooking_essential:\nMAIDA\nRS70 FOR 1000g\nRS40 FOR 500g")
            
        elif user_input in["RICE & POHA"]:
            print("cooking_essential:\nBASUMATHI\nSONA MASURI\nJEERA\nPOHA ")
        
        elif user_input in ["BASUMATHI"]:
            print("cooking_essential:\nBASUMATHI\nRS150 FOR 1000g\nRS80 FOR 500g")
            
        elif user_input in ["SONA MASURI"]:
            print("cooking_essential:\nSONA MASURI\nRS200 FOR 1000g\nRS100 FOR 500g")
            
        elif user_input in ["JEERA"]:
            print("cooking_essential:\nJEERA\nR85 FOR 1000g\nRS46 FOR 500g")
            
        elif user_input in ["POHA"]:
            print("cooking_essential:\nPOHA\nRS70 FOR 1000g\nRS40 FOR 500g")
            
        elif user_input in ["OIL & GHEE"]:
            print("cooking_essential:\nCOCONUT\nSUNFLOWER\nGROUND NUT\nMUSTARD\nGHEE ")
        
        elif user_input in ["COCONUT"]:
            print("cooking_essential:\nCOCONUT\nRS240 FOR 1l\nRS130 FOR 500ml")
            
        elif user_input in ["SUNFLOWER"]:
            print("cooking_essential:\nSUNFLOWER\nRS200 FOR 1l\nRS100 FOR 500ml")
            
        elif user_input in ["GROUND NUT"]:
            print("cooking_essential:\nGROUND NUT\nRS400 FOR 1l\nRS200 FOR 500ml")
            
        elif user_input in ["MUSTARD"]:
            print("cooking_essential:\nMUSTARD\nRS158 FOR 1l\nRS130 FOR 500ml")
            
        elif user_input in ["GHEE"]:
            print("cooking_essential:\nGHEE\nRS500 FOR 1l\nRS250 FOR 500ml")
            
        elif user_input in["DRY FRUITS"]:
            print("cooking_essentiaL:\nALMOND\nCASHEW\nRAISINS\nDATES ")
        
        elif user_input in["ALMOND"]:
            print("cooking_essential:\nALMOND\nRS400 FOR 1000g\nRS200 FOR 500g")
            
        elif user_input in["CASHEW"]:
            print("cooking_essential:\nCASHEW\nRS600 FOR 1000g\nRS300 FOR 500g")
            
        elif user_input in["RAISINS"]:
            print("cooking_essential:\nRAISINS\nRS180 FOR 1000g\nRS90 FOR 500g")
            
        elif user_input in["DATES"]:
            print("cooking_essential:\nDATES\nRS300 FOR 1000g\nRS150 FOR 500g")
            
        
        elif user_input in["SALT"]:
            print("cooking_essential:\nSALT\nRS26 FOR 1000g\nRS15 FOR 500g")
            
        elif user_input in["SUGAR"]:
            print("cooking_essential:\nSUGAR\nRS50 FOR 1000g\nRS25 FOR 500g")
            
        elif user_input in["JAGGERY"]:
            print("cooking_essential:\nJAGGERY\nRS60 FOR 1000g\nRS30 FOR 500g")
        
        else:
            print("cooking_essential: I'm not sure how to respond to this")
    
cooking_essential()