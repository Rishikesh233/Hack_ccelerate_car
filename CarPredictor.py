import streamlit as st  #importing libraries
import pickle 
import time
model = pickle.load(open('RF_model.pkl','rb'))  #importing the model that was trained using Random forest algo

def main(): #defining main function
    string = "CAR PRICE PREDICTOR"
    st.set_page_config(page_title=string, page_icon="🚗", layout = "wide") #setting configuration of web page
    st.title("Car Price Predictor")

    st.markdown(""" <style>
    #MainMenu {visibility: hidden;}        #For hiding the menu bar
    footer {visibility: hidden;}
    </style> """, unsafe_allow_html=True)

    padding = 0
    st.markdown(f""" <style>
    .reportview-container .main .block-container{{      #For condensing the page layout
        padding-top: {padding}rem;
        padding-right: {padding}rem;
        padding-left: {padding}rem;
        padding-bottom: {padding}rem;
    }} </style> """, unsafe_allow_html=True)

    st.markdown("##### This web application predicts the prices of cars based on your inputs. The model is trained using Random Forest algorithm.\n##### So let's try evaluating the price based on your inputs.")
    st.image(
            "https://media2.giphy.com/media/cWWwLuxISKDRMyuqGB/giphy.gif?cid=ecf05e47ar2uwxm3xvoc30ogvz4ks96bho6ksszjrjvhw2h8&rid=giphy.gif&ct=g",
            width=280, # Manually Adjust the width of the image as per requirement
               )
    st.write('')
    st.write('')
    with st.spinner('Prediction is being done!'):
        time.sleep(8)  # Loading spinner call so that user does not get bored
    power = st.number_input('The Engine Power ( in hp ):', 33,779, step = 4 , key = 'Power') #Taking numer input as power with upper and lower limit as 779 and 33 respectively
    displacement = st.number_input('The Engine Capacity ( in cc ):', 624 , 6752 , step = 8 , key = 'Displacement') #Taking displacement as input through number input with respective limits
    mileage = st.number_input('The mileage of car :', 3.4 , 28.4 , step = 0.5 , key = 'Mileage') #mileage as number input with respective limits
    airbags = st.radio("Number of airbags :",(0,1,2,3,4,5,6,7,8,9,10,14), key = 'Airbags') #number of airbags as radio input
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True) #For radio buttons to be horizontal
    seats = st.radio("Number of seats :",(2,4,5,6,7,8,9), key = 'Seats') #seats as radio input
    Manufacturer_Audi = st.selectbox('Which company do you want?', ('Tata', 'Datsun', 'Renault', 'Maruti Suzuki', 'Hyundai', 'Premier', 'Toyota',
                 'Nissan', 'Volkswagen', 'Ford', 'Mahindra', 'Fiat', 'Honda',
                 'Jeep' ,'Isuzu', 'Skoda', 'Audi', 'Dc', 'Mini',
                 'Jaguar', 'Bmw', 'Porsche', 'Lexus', 'Maserati','Lamborghini', 'Bentley',
                 'Ferrari', 'Force', 'Volvo' , 'Land Rover Rover' , 'Kia', 
                 'Mitsubishi', 'Maruti Suzuki R', 'Land Rover','Aston Martin'), key = 'Manufacturer') #Taking input of company name

    dict_manufacturer = {'Tata' : 30, 'Datsun' : 3, 'Renault':28, 'Maruti Suzuki' : 20, 'Hyundai' : 10, 'Premier':27, 'Toyota' : 31,
                 'Nissan' : 25, 'Volkswagen':32, 'Ford' : 8, 'Mahindra' : 19, 'Fiat' : 6, 'Honda' : 9,
                 'Jeep' : 13,'Isuzu' : 11, 'Skoda' : 29, 'Audi': 0, 'Dc' : 4, 'Mini' : 23,
                 'Jaguar' : 12, 'Bmw' : 2, 'Porsche' : 26, 'Lexus':18, 'Maserati' : 22,'Lamborghini':15, 'Bentley' : 1,
                 'Ferrari' : 5, 'Force' : 7, 'Volvo' : 33 , 'Land Rover Rover' : 17 , 'Kia': 14, 
                 'Mitsubishi' : 24, 'Maruti Suzuki R' : 21, 'Land Rover' : 16}   # I define a dictionary where company name is key and lexicographic order is value
                 #This dictionary would be furthur used.

    list_manufacturer = ['Manufacturer_Audi', 'Manufacturer_Bentley',
       'Manufacturer_Bmw', 'Manufacturer_Datsun', 'Manufacturer_Dc',
       'Manufacturer_Ferrari', 'Manufacturer_Fiat', 'Manufacturer_Force',
       'Manufacturer_Ford', 'Manufacturer_Honda', 'Manufacturer_Hyundai',
       'Manufacturer_Isuzu', 'Manufacturer_Jaguar', 'Manufacturer_Jeep',
       'Manufacturer_Kia', 'Manufacturer_Lamborghini',
       'Manufacturer_Land_Rover', 'Manufacturer_Land_Rover_Rover',
       'Manufacturer_Lexus', 'Manufacturer_Mahindra',
       'Manufacturer_Maruti_Suzuki', 'Manufacturer_Maruti_Suzuki_R',
       'Manufacturer_Maserati', 'Manufacturer_Mini',
       'Manufacturer_Mitsubishi', 'Manufacturer_Nissan',
       'Manufacturer_Porsche', 'Manufacturer_Premier',
       'Manufacturer_Renault', 'Manufacturer_Skoda', 'Manufacturer_Tata',
       'Manufacturer_Toyota', 'Manufacturer_Volkswagen',
       'Manufacturer_Volvo'] #A list of columns created by get_dummies function on our dataset. These will be n-1 where n be unique elements in that particular column
   
    list_feat = [] #Define an empty list
    if(Manufacturer_Audi != 'Aston Martin'): #Aston Martin does not get any dummy variable so exclusing it.
        if(Manufacturer_Audi):
            for i in range(34):
                if (dict_manufacturer[Manufacturer_Audi] != i): # When value from dictionary associated with input ( i.e. key ) then we append 1 to list.
                   list_feat.append(0)
                else:
                   list_feat.append(1)
        #For example, if user chooses car company as Mini, so value associated to Manufacturer Mini is 23. 
        # So list_feat[23] = 1 and rest all would be zero
            Manufacturer_Audi = list_feat[0]      #Here I need to write all variables individually as they would input in model later
            Manufacturer_Bentley = list_feat[1]
            Manufacturer_Bmw = list_feat[2]
            Manufacturer_Datsun = list_feat[3]
            Manufacturer_Dc = list_feat[4]
            Manufacturer_Ferrari = list_feat[5]
            Manufacturer_Fiat = list_feat[6]
            Manufacturer_Force = list_feat[7]
            Manufacturer_Ford = list_feat[8]
            Manufacturer_Honda = list_feat[9]
            Manufacturer_Hyundai = list_feat[10]
            Manufacturer_Isuzu = list_feat[11]
            Manufacturer_Jaguar = list_feat[12]
            Manufacturer_Jeep = list_feat[13]
            Manufacturer_Kia = list_feat[14]
            Manufacturer_Lamborghini = list_feat[15]
            Manufacturer_Land_Rover = list_feat[16]
            Manufacturer_Land_Rover_Rover = list_feat[17]
            Manufacturer_Lexus = list_feat[18]
            Manufacturer_Mahindra = list_feat[19]
            Manufacturer_Maruti_Suzuki = list_feat[20]
            Manufacturer_Maruti_Suzuki_R = list_feat[21]
            Manufacturer_Maserati = list_feat[22]
            Manufacturer_Mini = list_feat[23]
            Manufacturer_Mitsubishi = list_feat[24]
            Manufacturer_Nissan = list_feat[25]
            Manufacturer_Porsche = list_feat[26]
            Manufacturer_Premier = list_feat[27]
            Manufacturer_Renault = list_feat[28]
            Manufacturer_Skoda = list_feat[29]
            Manufacturer_Tata = list_feat[30]
            Manufacturer_Toyota = list_feat[31]
            Manufacturer_Volkswagen = list_feat[32]
            Manufacturer_Volvo = list_feat[33]
    
    #If input is Aston Martin then all variables will be equal to 0
    elif(Manufacturer_Audi == 'Aston Martin'):
        Manufacturer_Audi = 0
        Manufacturer_Bentley = 0
        Manufacturer_Bmw = 0
        Manufacturer_Datsun = 0
        Manufacturer_Dc = 0
        Manufacturer_Ferrari = 0
        Manufacturer_Fiat = 0
        Manufacturer_Force = 0
        Manufacturer_Ford = 0
        Manufacturer_Honda = 0
        Manufacturer_Hyundai = 0
        Manufacturer_Isuzu = 0
        Manufacturer_Jaguar = 0
        Manufacturer_Jeep = 0
        Manufacturer_Kia = 0
        Manufacturer_Lamborghini = 0
        Manufacturer_Land_Rover = 0
        Manufacturer_Land_Rover_Rover = 0
        Manufacturer_Lexus = 0
        Manufacturer_Mahindra = 0
        Manufacturer_Maruti_Suzuki = 0
        Manufacturer_Maruti_Suzuki_R = 0
        Manufacturer_Maserati = 0
        Manufacturer_Mini = 0
        Manufacturer_Mitsubishi = 0
        Manufacturer_Nissan = 0
        Manufacturer_Porsche = 0
        Manufacturer_Premier = 0
        Manufacturer_Renault = 0
        Manufacturer_Skoda = 0
        Manufacturer_Tata = 0
        Manufacturer_Toyota = 0
        Manufacturer_Volkswagen = 0
        Manufacturer_Volvo = 0
   
    #Taking input of fuel type: 
    #Defining these variables is necessary as i need to input these in model later
    Fuel_Type_Petrol = st.selectbox('What is the fuel type of the car ?',('Petrol','Diesel', 'Hybrid', 'CNG + Petrol'), key='Fuel_Type')
    if(Fuel_Type_Petrol=='Petrol'): #if selected is petrol then petrol type would be 1 and rest 0
        Fuel_Type_Petrol=1
        Fuel_Type_Diesel=0
        Fuel_Type_Hybrid=0
    elif(Fuel_Type_Petrol=='Diesel'): #if selected is diesel then diesel type would be 1 and rest 0
        Fuel_Type_Petrol=0
        Fuel_Type_Diesel=1
        Fuel_Type_Hybrid=0
    elif(Fuel_Type_Petrol=='Hybrid'): #if selected is hybrid then hybrid type would be 1 and rest 0
        Fuel_Type_Petrol=0
        Fuel_Type_Diesel=0
        Fuel_Type_Hybrid=1
    else:                    #if selected is CNG+Petrol then all would be 0
        Fuel_Type_Petrol=0
        Fuel_Type_Diesel=0
        Fuel_Type_Hybrid=0
    
    #Taking input of gear type:
    #Defining these variables is necessary as i need to input these in model later
    Gear_Type_Automatic = st.selectbox('What is gear type?',('Automatic','CVT','DCT','Manual','AMT'), key = 'Gear_Type')
    if(Gear_Type_Automatic=='Automatic'): #if selected is automatic then automatic type would be 1 and rest 0
        Gear_Type_Automatic=1
        Gear_Type_CVT = 0
        Gear_Type_DCT = 0
        Gear_Type_Manual=0
    elif(Gear_Type_Automatic=='CVT'): #if selected is CVT then CVT type would be 1 and rest 0
        Gear_Type_Automatic=0
        Gear_Type_CVT = 1
        Gear_Type_DCT = 0
        Gear_Type_Manual=0
    elif(Gear_Type_Automatic=='DCT'): #if selected is DCT then DCT Type would be 1 and rest 0
        Gear_Type_Automatic=0
        Gear_Type_CVT = 0
        Gear_Type_DCT = 1
        Gear_Type_Manual=0
    elif(Gear_Type_Automatic=='Manual'): #if selected is Manual then manual type would be 1 and rest 0
        Gear_Type_Automatic=0
        Gear_Type_CVT = 0
        Gear_Type_DCT = 0
        Gear_Type_Manual=1
    else: #if selected is AMT then all would be 0
        Gear_Type_Automatic=0
        Gear_Type_CVT = 0
        Gear_Type_DCT = 0
        Gear_Type_Manual=0
   
    #The logic behind these variable is same as earlier two inputs
    Drivetrain_AWD = st.selectbox('Select Drive Train:',('AWD (All Wheel Drive)','FWD (Front Wheel Drive)','RWD (Rear Wheel Drive)','4WD'), key = 'Drivetrain')
    if(Drivetrain_AWD == 'AWD (All Wheel Drive)'):
       Drivetrain_AWD = 1
       Drivetrain_FWD = 0
       Drivetrain_RWD = 0
    elif(Drivetrain_AWD == 'FWD (Front Wheel Drive)'):
       Drivetrain_AWD = 0
       Drivetrain_FWD = 1
       Drivetrain_RWD = 0
    elif(Drivetrain_AWD == 'RWD (Rear Wheel Drive)'):
       Drivetrain_AWD = 0
       Drivetrain_FWD = 0
       Drivetrain_RWD = 1
    else:
       Drivetrain_AWD = 0
       Drivetrain_FWD = 0
       Drivetrain_RWD = 0 

    if st.button("Estimate Price", key = 'predict'): #If user presses estimate price
        Model = model #get_model
        #using predict() and giving all variables as input and store that in prediction named variable
        prediction = Model.predict([[power,displacement,airbags,seats,mileage,Manufacturer_Audi,Manufacturer_Bentley,Manufacturer_Bmw,Manufacturer_Datsun,Manufacturer_Dc,Manufacturer_Ferrari,Manufacturer_Fiat,
                                        Manufacturer_Force,Manufacturer_Ford,Manufacturer_Honda,Manufacturer_Hyundai,Manufacturer_Isuzu,Manufacturer_Jaguar,Manufacturer_Jeep, Manufacturer_Kia,Manufacturer_Lamborghini,
                                        Manufacturer_Land_Rover,Manufacturer_Land_Rover_Rover,Manufacturer_Lexus,Manufacturer_Mahindra,Manufacturer_Maruti_Suzuki, Manufacturer_Maruti_Suzuki_R, Manufacturer_Maserati,
                                        Manufacturer_Mini,Manufacturer_Mitsubishi,Manufacturer_Nissan,Manufacturer_Porsche, Manufacturer_Premier,Manufacturer_Renault,Manufacturer_Skoda,Manufacturer_Tata,Manufacturer_Toyota,
                                        Manufacturer_Volkswagen,Manufacturer_Volvo,Fuel_Type_Petrol,Fuel_Type_Diesel,Fuel_Type_Hybrid,Gear_Type_Automatic, Gear_Type_CVT,Gear_Type_DCT, Gear_Type_Manual,Drivetrain_AWD,Drivetrain_FWD,Drivetrain_RWD]])
        output = round(prediction[0],2) #Taking output as rounding off to 2 decimal places
        if output < 0: #there might be case where output is less than 0 so giving warning as
            st.warning("Price of car having such inputs can not be estimated !!")

        else: #otherwise show the estimated aprroximated price
            st.success("The price of such car would be roughly around ₹{} ".format(output))  
        
        st.snow() #animated snow throughout the screen

if __name__ == '__main__': #calling main function 
    main()
