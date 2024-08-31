import pandas as pd

india = {
    'state':['West Bengal','Rajasthan','Jammu And Kashmir','Uttar Pradesh','Bihar','Assam','Odisha','Tamil Nadu','Andra Pradesh', 'Madhya Pradesh', 'Kerala', 'Karnataka','Maharashtra', 'Gujarat','Nagaland', 'Punjab', 'Himachal Pradesh', 'Manipur', 'Meghalaya', 'Tripura', 'Sikkim', 'Goa', 'Arunachal Pradesh', 'Mizoram', 'Chattisgarh', 'Jharkhand', 'Uttarkhand', 'Telangana', 'Delhi', 'Andaman And Nicobar', 'Dadar And nagar Haveli', 'Daman And Diu', 'Lakshadweep', 'Puducherry', 'Ladhakh', 'Haryana'],
    'x':[89, -143, -107, -32, 51, 156, 30, -70, -53, -61, -99, -111, -118, -169, 187, -105, -71, 179, 122, 140, 90, -138, 181, 166, -8, 36, -46, -57, -79, 174, -161, -187, -172, -45, -62, -93],
    'y':[26, 103, 200, 86, 64, 85, -17, -180, -118, 26, -196, -118, -32, 35, 82, 163, 181, 56, 70, 37, 105, -104, 126, 32, 3, 37, 147, -65, 118, -191, -7, -37, -183, -166, 232, 132]
}

ind_data = pd.DataFrame(india)
ind_data.to_csv('test.csv')
print(ind_data)