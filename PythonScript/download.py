import requests
import re
import sys
import difflib
# the program extracts text and image data for a given topic
# and writes them in the CURRENT DIRECTORY, relative to the location the py script is invoked from
# make sure you set it properly, in case you dont want the default one

# this is the title we will search

import os

workingdirectory = os.getcwd()

#print(sys.argv[2])
#nouns = "[.apple, 5.5/Apple/26, 99_Apples, @Apple, @AppleMusic, @Applebees, A6_apple, AJ_Applegate, APPLE, ATG_(Apple), A_For_Apple, A_for_Apple, Adam's_Apple, Adam's_Apples, Adam's_apple, Adam_Apple, Adams'_apple, Adams_Apple, Adams_Apples, Adams_apple, Adem's_Apple, Adem's_apple, Adems_Apple, Adems_apple, Affy_tapple, Akane_(apple), Alex_Chapple, Alf_Appleton, Amy_Applegren, And_Mapple, Andrew_Apple, Andy_Mapple, Anita_Appleby, Ann_Applebaum, Anna_(apple), Anne_Appleby, Ap_Applewhite, Apple, Apple's_Jade, Apple's_Way, Apple,_Fiona, Apple,_Inc, Apple,_Inc., Apple,_inc., Apple,inc., Apple-1, Apple-2, Apple-CAT_II, Apple-Cat_II, Apple-Intel, Apple-Kneel, Apple-Oids, Apple-head, Apple-leaf, Apple-maggot, Apple-of-Peru, Apple-peru, Apple-pie, Apple-scab, Apple-shot, Apple-tree, Apple.com, Apple.news, Apple2gs, Apple:_iPod, AppleBus, AppleCD, AppleCD_SC, AppleCard, AppleCare, AppleCare+, AppleCat, AppleCat_II, AppleComputer, AppleDOS, AppleDaily, AppleDouble, AppleEvent, AppleEvents, AppleID, AppleInc., AppleInsider, AppleJack, AppleLink, AppleMail, AppleMaster, AppleMasters, AppleNet, AppleNova, ApplePay, AppleRecords, AppleScript, AppleSearch, AppleShare, AppleShare_IP, AppleShare_PC, AppleSingle, AppleTV, AppleTV+, AppleTalk, AppleTree, AppleWebKit, AppleWin, AppleWorks, AppleWriter, Apple_&_Onion, Apple_(Fruit), Apple_(Japan), Apple_(album), Apple_(band), Apple_(fruit), Apple_(name), Apple_(song), Apple_(store), Apple_(tree), Apple_(wine), Apple_//, Apple_///, Apple_//c, Apple_//e, Apple_1, Apple_11, Apple_2, Apple_2C, Apple_2GS, Apple_2c, Apple_2e, Apple_3, Apple_871, Apple_A10, Apple_A10X, Apple_A11, Apple_A12, Apple_A12X, Apple_A12Z, Apple_A13, Apple_A14, Apple_A1661, Apple_A4, Apple_A4_chip, Apple_A5, Apple_A5X, Apple_A5_Chip, Apple_A5x, Apple_A6, Apple_A6X, Apple_A7, Apple_A8, Apple_A8X, Apple_A9, Apple_A9X, Apple_ATG, Apple_Air, Apple_AirPlay, Apple_AirPods, Apple_AirPort, Apple_Airpods, Apple_Airport, Apple_Andy, Apple_Annie, Apple_Arcade, Apple_Ax, Apple_BASIC, Apple_Backup, Apple_Banana, Apple_Bank, Apple_Bed, Apple_Beer, Apple_Berry, Apple_Bite, Apple_Bloom, Apple_Blossom, Apple_Bomb, Apple_Bonjour, Apple_Books, Apple_Bottom, Apple_Bottoms, Apple_Bowl, Apple_Box, Apple_Brook, Apple_Byte, Apple_CD, Apple_CP/M, Apple_Campus, Apple_Car, Apple_CarPlay, Apple_Card, Apple_Cards, Apple_Care, Apple_Cash, Apple_Cat, Apple_Chan, Apple_Chase, Apple_Chess, Apple_Chill, Apple_Chip, Apple_Chips, Apple_Chooser, Apple_Cobbler, Apple_Color, Apple_Comics, Apple_Company, Apple_Connect, Apple_Console, Apple_Corp, Apple_Corp., Apple_Corps, Apple_Creek, Apple_Crisp, Apple_Crumble, Apple_Cube, Apple_Cup, Apple_Cyclone, Apple_DOS, Apple_DOS_3.0, Apple_DOS_3.1, Apple_DOS_3.2, Apple_DOS_3.3, Apple_DRM, Apple_Daily, Apple_Darwin, Apple_Day, Apple_Device, Apple_Disk_II, Apple_DuoFile, Apple_Dylan, Apple_EMac, Apple_EarPod, Apple_EarPods, Apple_Earbuds, Apple_Energy, Apple_Ermine, Apple_Event, Apple_Events, Apple_Expo, Apple_Express, Apple_Eyes, Apple_FM, Apple_Fellow, Apple_Films, Apple_Finder, Apple_Fire, Apple_Front, Apple_G4, Apple_GCR, Apple_GS/OS, Apple_Gabriel, Apple_Grab, Apple_Grapher, Apple_Green, Apple_Grove, Apple_Guava, Apple_Guide, Apple_H1, Apple_HFS, Apple_HFS+, Apple_Head, Apple_Health, Apple_Hill, Apple_History, Apple_HomeKit, Apple_HomePod, Apple_Homekit, Apple_Hong, Apple_Huang, Apple_I, Apple_ID, Apple_II, Apple_II+, Apple_IIC, Apple_IIGS, Apple_III, Apple_III+, Apple_II_GS, Apple_II_Plus, Apple_II_plus, Apple_IIc, Apple_IIc+, Apple_IIe, Apple_IIgs, Apple_IIx, Apple_IIÉ¢s, Apple_IIâ??, Apple_IMC, Apple_IWM, Apple_Inc, Apple_Inc., Apple_India, Apple_Insider, Apple_Intel, Apple_Island, Apple_Isle, Apple_Jack, Apple_Jacks, Apple_Jam, Apple_Juice, Apple_Key, Apple_Keynote, Apple_Kid, Apple_Kim, Apple_Lane, Apple_Leopard, Apple_Line, Apple_Lisa, Apple_Lisa_2, Apple_Logic, Apple_Logo, Apple_Looper, Apple_M10, Apple_M12, Apple_M7, Apple_M8, Apple_M9, Apple_Mac, Apple_MacBook, Apple_MacOSX, Apple_Mac_G4, Apple_Mac_OS, Apple_Mac_OSX, Apple_Mac_Pro, Apple_Macbook, Apple_Macs, Apple_Maggot, Apple_Mail, Apple_Maps, Apple_Market, Apple_Martin, Apple_Mary, Apple_Master, Apple_Masters, Apple_McRory, Apple_Menu, Apple_Metal, Apple_Miyuki, Apple_Modem, Apple_Moss, Apple_Motion, Apple_Mouse, Apple_Music, Apple_Music_1, Apple_Nano, Apple_NetBoot, Apple_News, Apple_News+, Apple_Newton, Apple_Newtons, Apple_Notes, Apple_Numbers, Apple_O, Apple_O', Apple_OS, Apple_OSX, Apple_OS_X, Apple_Oids, Apple_One, Apple_Pages, Apple_Paladin, Apple_Panic, Apple_Park, Apple_Pascal, Apple_Pay, Apple_PenLite, Apple_Pencil, Apple_Penne, Apple_Photos, Apple_Pie, Apple_Pie_ABC, Apple_Pink, Apple_Pippen, Apple_Pippin, Apple_Podcast, Apple_Pope, Apple_PowerCD, Apple_Press, Apple_Preview, Apple_ProDOS, Apple_ProFile, Apple_ProRes, Apple_Punch, Apple_Qmaster, Apple_RGB, Apple_Records, Apple_Remote, Apple_ResEdit, Apple_Retail, Apple_River, Apple_Rose, Apple_Rosetta, Apple_Rumours, Apple_S1, Apple_S1P, Apple_S2, Apple_S3, Apple_S4, Apple_S5, Apple_S6, Apple_SIM, Apple_SMC, Apple_SOS, Apple_Safari, Apple_Sauce, Apple_Scanner, Apple_Script, Apple_Scruffs, Apple_Search, Apple_Shake, Apple_Shampoo, Apple_Silicon, Apple_Siri, Apple_Snail, Apple_Springs, Apple_Store, Apple_Stores, Apple_Studio, Apple_Studios, Apple_Support, Apple_Swift, Apple_Switch, Apple_Symbols, Apple_T1, Apple_T2, Apple_TV, Apple_TV+, Apple_TV_+, Apple_TV_4K, Apple_TV_App, Apple_TV_OS, Apple_TV_OS_1, Apple_TV_OS_2, Apple_TV_OS_3, Apple_TV_OS_4, Apple_TV_OS_5, Apple_TV_OS_6, Apple_TV_OS_7, Apple_TV_OS_8, Apple_TV_Plus, Apple_TV_app, Apple_TV_plus, Apple_Tablet, Apple_Tavern, Apple_Team, Apple_Teams, Apple_Theif, Apple_Thief, Apple_Titan, Apple_Tomotsu, Apple_Tortrix, Apple_Travel, Apple_Tree, Apple_Trees, Apple_Trek, Apple_Tummy, Apple_Twiggy, Apple_Two, Apple_U1, Apple_UniFile, Apple_Valley, Apple_Venus, Apple_Video, Apple_W1, Apple_W2, Apple_W3, Apple_WALT, Apple_Wallet, Apple_War, Apple_Wassail, Apple_Watch, Apple_Watch_2, Apple_Watch_3, Apple_Wedding, Apple_White, Apple_Works, Apple_Worm, Apple_Writer, Apple_X11, Apple_Xcode, Apple_a, Apple_account, Apple_acid, Apple_alex, Apple_aphid, Apple_arcade, Apple_bananas, Apple_barn, Apple_berry, Apple_blossom, Apple_bobbing, Apple_bolete, Apple_bong, Apple_bottom, Apple_bottoms, Apple_box, Apple_brandy, Apple_butter, Apple_cactus, Apple_cake, Apple_cakes, Apple_campus, Apple_car, Apple_carbon, Apple_card, Apple_chill, Apple_chip, Apple_chips, Apple_cider, Apple_cobbler, Apple_comp, Apple_company, Apple_core, Apple_corer, Apple_creek, Apple_crisp, Apple_crisps, Apple_crumble, Apple_cube, Apple_cult, Apple_day, Apple_device, Apple_doll, Apple_dolls, Apple_drink, Apple_drop, Apple_drops, Apple_eMate, Apple_earbuds, Apple_eater, Apple_ermine, Apple_essence, Apple_event, Apple_events, Apple_expo, Apple_family, Apple_fanboy, Apple_flour, Apple_font, Apple_fonts, Apple_fritter, Apple_genome, Apple_green, Apple_guava, Apple_gum, Apple_homekit, Apple_hong, Apple_hq, Apple_i-phone, Apple_iBook, Apple_iBooks, Apple_iCal, Apple_iCar, Apple_iChat, Apple_iFund, Apple_iMac, Apple_iMovie, Apple_iOS, Apple_iOS_12, Apple_iPad, Apple_iPad_2, Apple_iPad_3, Apple_iPad_4, Apple_iPencil, Apple_iPhone, Apple_iPod, Apple_iPod+HP, Apple_iPod_ad, Apple_iPods, Apple_iRadio, Apple_iSync, Apple_iTV, Apple_iTouch, Apple_iTunes, Apple_iWatch, Apple_iWeb, Apple_iWork, Apple_icar, Apple_id, Apple_ii, Apple_iiGS, Apple_iic, Apple_iie, Apple_iigs, Apple_inc, Apple_inc., Apple_ipad, Apple_iphone, Apple_ipod, Apple_itv, Apple_jack, Apple_jam, Apple_juice, Apple_ketal, Apple_key, Apple_lisa, Apple_logo, Apple_looper, Apple_mac, Apple_macOS, Apple_maggot, Apple_mail, Apple_mallee, Apple_maps, Apple_martini, Apple_menu, Apple_mini, Apple_mint, Apple_moss, Apple_mouse, Apple_murex, Apple_of_Cain, Apple_of_Eden, Apple_of_Peru, Apple_of_peru, Apple_oil, Apple_orchard, Apple_os_x, Apple_outline, Apple_pc, Apple_pear, Apple_peel, Apple_peeler, Apple_phone, Apple_picking, Apple_pie, Apple_pies, Apple_pipe, Apple_printer, Apple_pudding, Apple_records, Apple_remote, Apple_rose, Apple_rumors, Apple_russet, Apple_rust, Apple_s_3, Apple_sauce, Apple_sawfly, Apple_scab, Apple_scald, Apple_screw, Apple_scruffs, Apple_seed, Apple_shake, Apple_shape, Apple_shop, Apple_shot, Apple_silicon, Apple_siri, Apple_slate, Apple_slicer, Apple_snail, Apple_soup, Apple_sphinx, Apple_springs, Apple_store, Apple_strudel, Apple_suits, Apple_talk, Apple_tart, Apple_timer, Apple_tortrix, Apple_tree, Apple_trees, Apple_tube, Apple_tummy, Apple_tv, Apple_v._Does, Apple_v_Apple, Apple_watch, Apple_wine, Apple_worm, Applebaum, Applebay, Applebay_Zia, Applebay_Zuni, Applebe's, Applebee, Applebee's, Applebees, Applebeeâ€™s, Appleberry, Applebite, Appleblim, Applebloom, Applebottoms, Applebox, Applebutter, Appleby, Appleby,_John, Appleby,_ON, Appleby,_Paul, Appleby,_TX, Appleby_Court, Appleby_Fells, Appleby_Group, Appleby_Hall, Appleby_Lodge, Appleby_Magna, Appleby_Parva, Appleby_magna, Appleby_parva, Applebyshire, Applecactus, Applecard, Applecare, Applecrab, Applecrest, Applecross, Appledale, Appledene, Appledoe, Appledoorn, Appledore, Appledore_FC, Appledore_F_C, Appledore_II, Appledorn, Appledouble, Appledram, Applefest, Applefield, Appleford, Applefront, Applegarth, Applegate, Applegate,_CA, Applegate,_MI, Applegate,_Mi, Applegate,_Or, Applegate_Dam, Applegath, Applegreen, Applegren, Applegrove, Applehead, Applehead_Man, Applehead_cat, Appleheads, AppleiOS, Appleinc, Appleinc., Appleinsider, Applejack, Applejack_hat, Applejacks, Applejaxx, Applejuice, Applelink, Appleman, Applemaster, Applemasters, Applemore, Appleoids, Applepie, Appler, Applera, Applera_Corp, Applera_Corp., Apples, Apples,_Vaud, Apples,_Vd, Apples,_vaud, Apples_(Vaud), Apples_(film), Apples_(song), Apples_CH, Apples_VD, Apples_Vaud, Apples_way, Applesac, Applesauce, Applesause, Applescript, Appleseed, Appleseed_DX, Appleseed_EX, Appleseed_OAV, Appleseed_OVA, Appleseed_Î±, Appleshaw, Applesingle, Applesoft, Applet, AppletViewer, Appletalk, Appletee, Applethorpe, Applethwaite, Appletini, Appletise, Appletiser, Appletizer, Appleton, Appleton's, Appleton,_IL, Appleton,_ME, Appleton,_MN, Appleton,_WI, Appleton,_Wi, Appleton_(WI), Appleton_City, Appleton_Dock, Appleton_Farm, Appleton_Post, Appleton_Road, Appleton_rum, Appletons', Appletown,_MD, Appletree, Appletreehall, Appletreewick, Applets, Applett, Appletun, Appletv, Appletviewer, Applewhite, Applewhites, Applewold, Applewold,_PA, Applewold,_Pa, Applewood, Applewood,_CO, Appleworks, Appley, Appley_Bridge, Appley_House, Appley_Towers, Appleyard, AppleÂ®, Arctic_Apple, Arctic_Apples, Arctic_apple, Arctic_apples, Argyle_apple, Asiatic_apple, Augusta_Apple, Bacardi_apple, Bad_Apple, Bad_Apple!!, Bad_apple, Bad_apples, Bake_apple, Bakeapple, Baked_apple, Baldwin_apple, Balmawhapple, Balsam-apple, Balsam_apple, Balsamapple, Banapple_Gas, Banapple_gas, Bapple_Donuts, Baron_Chapple, Barry_Appleby, Beach_apple, Beach_apples, Bell_Apple, Bell_apple, Ben_Appleby, Big_Apple, Big_Apple_Con, Big_Pineapple, Big_apple, Billy_Apple, Bitter-apple, Bitter_Apples, Bitter_apple, Black_Apple, Black_apple, Bob_Appleby, Bob_Appleyard, Bob_the_apple, Bobby_Appleby, BootX_(Apple), Boquhapple, Boycott_Apple, Bramley_apple, Brian_Chapple, Cactus_apple, Cairnpapple, Call-APPLE, Cameo_(apple), Cameo_apple, Canada_Apple, Canada_apple, Candied_apple, Candy_Apple, Candy_Apples, Candy_apple, Candy_apples, Cane_apple, Capplebarrow, Caramel_Apple, Caramel_apple, Carmel_apple, Carmel_apples, Cashew_apple, Chapple, Chapple,_John, Chapples_Park, Chinese_Apple, Chinese_apple, Chinkee_apple, Chris_Apple, Chris_Kappler, Cider_apple, Civni_apple, Cloud_apple, Cocky_apple, Coconut_apple, Colette_Apple, Colin_Appleby, Conch_apple, Cooking_Apple, Cooking_apple, Crab-apple, Crab_Apple, Crab_apple, Crab_apples, Crabapple, Crabapple,_GA, Crabapples, Cranapple, Crapple_Cup, Crapplet, Crispin_apple, Cult_Apple, Custard-apple, Custard_Apple, Custard_apple, D._Appleton, DML_Appledore, Dahabenzapple, Dale_Appleby, Dan_Applegate, Dapple, Dapple-grey, Dapple-throat, Dapple_gray, Dapple_grey, Dappled_white, Dapplegrim, Dapplethroat, Dave_Chapple, David_Chapple, David_J_Apple, Deadly_Apples, Deadly_apples, Deena_Mapple, Dessert_apple, Devil's_Apple, Devil's_apple, Devils_Apple, Devils_apple, Dole_pinapple, Dried_apple, Dudi_Appleton, Dwarf_apple, Earth_apple, East_Appleton, Ed_Appleton, Ed_Wineapple, Eli_Apple, Eliot_Chapple, Emma_Appleton, Empire_apple, Emu_apple, Emu_apples, Envy_(apple), Epic_vs_Apple, Epol/Apple, Erik_Apple, Eva_(apple), Eve's_apple, Eve_the_Apple, F._Chapple, FBI_v._Apple, FBI_v._apple, FBI_v_Apple, Father_Mapple, Files_(Apple), FionaApple, Fiona_Apple, Fiona_apple, Fionna_Apple, Flapple, Flynn_Appleby, Frank_Appleby, Frank_Chapple, Fred_Appleby, Fuji_(apple), Fuji_apple, Fuji_apples, G3_Apple, G4_Apple, G4_Apples, G5(Apple), G5_(Apple), GO_Appleby, GRNappletree, Gala_(apple), Gala_apple, Gala_apples, Geoff_Chapple, Glen_Chapple, Goat-apple, Goat_Apple, Goat_apple, Gold_Apple, Gold_apple, Golden_Apple, Golden_Apples, Golden_apple, Gooapple, Gopher_apple, Gowkthrapple, Grapple, Grapple_Beam, Grapple_Plant, Grapple_X, Grapple_Y, Grapple_Z, Grapple_droid, Grapple_plant, Grapple_truck, Grappler, Grappler_Baki, Grapplers, Grappletail, Green_Apple, Green_Apples, Green_apple, Green_apples, Grnappletree, Ground_apple, HFS_(Apple), HMS_Appledore, HMS_Grappler, HP_Apple, HP_Apple_V2, HP_Big_Apple, HP_Mid_Apple, Hag_apple, Hale_Appleman, Hale_appleman, Happy_Apple, Harry_Wappler, Hawley_apple, Heather_Apple, Hedge-apple, Hedge_apple, Hedgeapple, Hello_(Apple), Henry_Apple, Hey_Apple, Hog_apple, Hogapple, Holsapple, Home_(Apple), Horse-apple, Horse_apple, Horseapple, Hot_Apple_Pie, IAd_(Apple), IOS_(Apple), IOS_Apple, ITV_(Apple), IWM_(Apple), Ian_Appleyard, Ice_apple, Indian-apple, Indian_apple, Indo_(apple), Inside_Apple, Intel_Apple, Ios_(Apple), JJ_Appleton, JW_Appleyard, Jack_Appleton, Jack_Chapple, Jack_Kappler, Jacki_Apple, James_Chapple, Java.applet, Java_Apple, Java_Applet, Java_Applets, Java_apple, Java_applet, Java_applets, Jay_Appleton, Jazz_(apple), Jazz_apple, Jean_Appleton, Jeff_Knapple, Jem_Chapple, Jesse_Appler, Jill_Trappler, Jim_Apple, Jim_Appleby, Jo_Appleby, Joe_Appleton, Joe_appleton, Johann_Appler, John_Appleby, John_Appleton, John_Chapple, John_Kappler, Johnny_Apple, Jon_Applebaum, Jon_Appleton, Jon_Chapple, Joya_apple, Joyce_Appleby, Jubilee_apple, Jude_Appleton, June_Appleby, Jupiter_Apple, Jw_appleyard, KA_Applegate, K_A_Applegate, Kai_apple, Kanzi_(apple), Kanzi_apple, Kappler, Kappler,_John, Karen_Chapple, Katy_(apple), Katy_apple, Kei-apple, Kei_apple, Ken_Appleby, Ken_Appledorn, Kepel_apple, Kienapple_v_R, Kim_Appleby, Krabapple, LEDApple, LED_Apple, Lady_apple, Led_Apple, Ledapple, Lee_Chapple, Len_Appleton, Les_Appleton, Les_Chapple, Lisa_(Apple), Lisa_Appleton, Little_Apple, Liz_Appleby, Lodi_(apple), Lois_Appleby, Louis_Appleby, Love-apple, Love_Apple, Love_apple, Lucy_Appleby, Luke_Appleton, MN55_(apple), Mac_(Apple), Mack's_Apples, Macks_apples, Macoun_Apple, Macoun_apple, Mail_(Apple), Malacca_apple, Malay-Apple, Malay-apple, Malay_Apple, Malay_apple, Malayapple, Malinda_Apple, Malinda_apple, Mamee_apple, Mamey_apple, Mammee_Apple, Mammee_apple, Mammey_apple, Mapple, Mapple_Store, Mapplethorpe, Mappleton, Mapplewell, Mark_Appleman, Martin_Apple, Mary_Applebey, Mary_Appleby, Mary_Appleton, Matty_Appleby, Max_Apple, Max_Happle, Max_apple, May-apple, May_apple, Mayapple, Mayapple_rust, Mel_appleby, Melba_(apple), Melon_(apple), Michael_Apple, Midget_Apple, Mike_Apple, Mike_Appleton, Monkey-apple, Monkey_apple, Mountainapple, Ms._Crabapple, Mud_&_Apples, Mulga_apple, Mutsu_(apple), Mutsu_apple, Nancy_Apple, Nancy_apple, Napple, Napple_Tale, News_(Apple), Newtons_apple, Notes_(Apple), Nun_Appleton, Nunappleton, Oak-apple, Oak-apple_Day, Oak_Apple_Day, Oak_apple, Oak_apples, Old_Appleton, One_Bad_Apple, One_bad_apple, Opal_(apple), Open-Apple, Open-apple, Open_Apple, Open_apple, Osage-apple, Osage_Apple, Osage_apple, Pages_(Apple), Pandapple, Papple, Papplewick, Pat_Apple, Pat_Appleyard, Paul_Appleby, Paula_apple, Peeled_Apples, Pete_Appleton, Phil_Chapple, Picon_(Apple), Pinata_apple, Pine-Apple, Pine_Apple, Pine_apple, Pineapple, Pineapple_Air, Pineapple_Bun, Pineapple_Man, Pineapple_Pen, Pineapple_Pit, Pineapple_RV, Pineapple_bun, Pineapple_gel, Pineapple_pen, Pineapple_pit, Pineapplefish, Pineapples, Pineapplette, Pineappleweed, Pink_(Apple), Pink_Apple, Pippin_apple, Pitch-apple, Point_Appleby, Poison-apple, Poison_Apple, Poison_apple, Pond-apple, Pond_apple, Pratt_apple, Prima_(apple), Prima_apple, Punic_apple, R.W._Apple, R._Apple, R._W._Apple, RAF_Appledram, RFA_Appleleaf, RW_Apple,_Jr., Rajka_(apple), Rambo_apple, Rapple, Rappler, Rappler.com, Rapples_Pan, Ray_Appleton, Raymond_Apple, Red_Apple, Red_Applegate, Red_Apples, Red_Pineapple, Red_apple, Red_apples, Red_pineapple, Redlove_apple, Rex_Applegate, Road_Apples, Road_apple, Road_apples, Roadapple, Roadapples, Rob_Appleby, Rob_Appleyard, Robin_Chapple, Rod_Appleton, Rome_apple, Rose-apple, Rose_Apple, Rose_apple, Roseapple, Ross_Appleton, Rotten_Apple, Rotten_Apples, Rotten_apple, Roy_Applegate, Roy_Appleyard, Rubens_apple, Russet_apple, Ruth_Appleby, Rw_apple, S.V._Appleby, SKAppleton, STK_applet, Safari_apple, Sam_Apple, Sam_Apple_Pie, Sand-apple, Sand_Apple, Sand_apple, Sansa_apple, Sappleton, Scrapple, ScrappleFace, Sea_apple, Sea_pineapple, Senator_Apple, Sharon_Apple, Shaun_Chapple, Sheldapple, Shellapple, Sheri_Appleby, Shiri_Appleby, Shrub_apple, Sid_Applebaum, Sievers_apple, Silver_Apples, Silver_apples, Silver_dapple, Simon_Apple, Simply_Apple, Siri_(Apple), Skappleton, Smudgy_apple, Snap_Apple, Snap_apple, Snapple, Snapple_Facts, Snapple_facts, Snapple_lady, Soda_Apple, Soda_apple, Sodom_apple, Sodom_apples, Solid-apple, Solid_apple, Sorb_apple, Sorry_Apple, Soup_(Apple), Sour_Apple, Sour_Apples, Sour_apple, Spartan_apple, Spring_apples, Squaw_apple, Star_Apple, Star_apple, Starapple, Stayman_apple, Stolen_Apples, Stone_apple, Sugar-apple, Sugar_Apple, Sugar_apple, Sugared_apple, Susie_Appleby, Swaysie_apple, Swayzie_apple, Sweet_Apple, Sweet_apple, Sweetapple, TV_(Apple), Table_apple, Taffy_apple, Taffy_apples, Tea_crabapple, TheAppleBlog, The_Apple, The_Apple_Bed, The_Apple_Cup, The_Apple_Pan, The_Apple_War, The_Applecart, The_Apples, The_Big_Apple, The_Grapple, The_Grappler, The_Grapplers, The_Pineapple, The_Red_Apple, The_big_apple, Thorn-apple, Thorn_apple, Thorn_apples, Thornapple, Tim_Apple, Titan_(Apple), Toffee_Apple, Toffee_apple, Toffee_apples, Tom_Apple, Tony_Appleton, Topaz_(apple), USS_Grapple, US_v._Apple, Van_Appledorn, Velvet-apple, Velvet_Apple, Velvet_apple, W._A._Chapple, Waltz_(Apple), Water-Apple, Water-apple, Water_Apple, Water_apple, Waterapple, Wax-Apple, Wax-apple, Wax-apples, Wax_apple, Waxapple, Waxapples, Wealthy_Apple, Weird_apples, Welsh_Apple, Welsh_Apples, Welsh_apple, Welsh_apples, White_Apple, White_Apples, White_apple, Wi_apple, Wiapple, Wild_Apple, Wild_apple, Will_Appleton, Winter_Apple, Winter_apple, Wolf-apple, Wolf_Apple, Wolf_apple, Wolfapple, Wood-apple, Wood_Apple, Wood_apple, Woodapple, Www.apple.com, X3D_Applet, York_Apple, York_apple, Zach_Apple, Zachary_Apple, Zapple, Zestar_Apple, Zestar_apple]"
#nouns = sys.argv[1]
#nounarray = nouns.lower().replace("[", "").replace("]", "").split(", ", len(nouns))
#print(nounarray)

topic = "hospital"

# this is the config for to get the first introduction of a title
text_config = {
    'action': 'query',
    'format': 'json',
    'titles': topic,
    'prop': 'extracts',
    'exintro': True,
    'explaintext': True,
}
text_response = requests.get('https://en.wikipedia.org/w/api.php', params=text_config).json()
text_page = next(iter(text_response['query']['pages'].values()))

print(text_page['extract'])

file1 = open("TextFiles/" + text_page['title'].lower() + ".txt", "w")  # write mode
file1.write(text_page['extract'])
file1.close()

"""
#this is the config to get the images that are in the topic
#we use this to count the number of images
num_image_config = {
    'action': 'parse',
    'pageid': text_page['pageid'],
    'format': 'json',
    'prop': 'images'
}
num_image_response = requests.get('https://en.wikipedia.org/w/api.php',params=num_image_config).json()



#now that we have the number of images in the page, we ask for the images that are in the page with the title
image_config = {
    'action': 'query',
    'format': 'json',
    'titles': topic,
    'prop': 'images',
    'imlimit': len(num_image_response['parse']['images'])
}
image_response = requests.get('https://en.wikipedia.org/w/api.php',params=image_config).json()
image_page = next(iter(image_response['query']['pages'].values()))


#and we  write the image files one by one in the currect directory
#we also dont write the svg files, since as they are mostly the logos
#modily the filename_pattern regex for to accept the proper files
#print("writing files")
filename_pattern = re.compile(".*\.(?:jpe?g|gif|png|JPE?G|GIF|PNG)")
for i in range(len(image_page['images'])):
    
    url_config = {
        'action': 'query',
        'format': 'json',
        'titles': image_page['images'][i]['title'],
        'prop': 'imageinfo',
        'iiprop': 'url'
    }
    url_response = requests.get('https://en.wikipedia.org/w/api.php',params=url_config).json()
    url_page = next(iter(url_response['query']['pages'].values()))
    #print(url_page['imageinfo'][0]['url'])
    if(filename_pattern.search(url_page['imageinfo'][0]['url'])):

        #print("writing image "+url_page['imageinfo'][0]['url'].rsplit("/",1)[1])
        with open(url_page['imageinfo'][0]['url'].rsplit("/",1)[1], 'wb') as handle:
            response = requests.get(url_page['imageinfo'][0]['url'], stream=True)

            if not response.ok:
                #print (response)
                print()
            for block in response.iter_content(1024):
                if not block:
                    break

                handle.write(block)

"""
# ************************************references*******************************************************************
# https://www.mediawiki.org/wiki/API:Parsing_wikitext
# https://www.mediawiki.org/wiki/Extension:TextExtracts#Caveats
# https://stackoverflow.com/questions/58337581/find-image-by-filename-in-wikimedia-commons
# https://en.wikipedia.org/w/api.php?action=query&titles=File:Albert_Einstein_Head.jpg&prop=imageinfo&iiprop=url

# https://stackoverflow.com/questions/24474288/how-to-obtain-a-list-of-titles-of-all-wikipedia-articles
# for all titles
# https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-all-titles-in-ns0.gz
# https://en.wikipedia.org/w/api.php?action=parse&pageid=252735&prop=images
