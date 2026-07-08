import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Set seed for reproducibility
np.random.seed(42)
random.seed(42)

# Number of rows
n_rows = 1000

# 1. User IDs
user_ids = [f"USER_{str(i).zfill(4)}" for i in range(1, n_rows + 1)]

# 2. Device Types
device_types = np.random.choice(
    ['Smartphone', 'Laptop', 'Tablet', 'Smart TV', 'IoT Device'],
    n_rows,
    p=[0.50, 0.25, 0.10, 0.08, 0.07]
)

# 3. Locations (One Specific Area: "Downtown Tech District")
locations = np.random.choice(
    [
        'TechHub_Cafe', 'Innovation_Park_Gate', 'CoWorking_Space_A', 
        'Main_Square_WiFi', 'Metro_Station_Exit', 'City_Library_Zone', 
        'Food_Court_WiFi', 'Gym_Lobby', 'Central_Park_Bench', 'Shopping_Mall_Entrance'
    ],
    n_rows
)

# 4. Authentication Methods
auth_methods = np.random.choice(
    ['WPA2-Enterprise', 'Captive Portal', 'Social Login', 'OTP Verification'],
    n_rows,
    p=[0.40, 0.30, 0.20, 0.10]
)

# 5. Subscription Plans
subscription_plans = np.random.choice(
    ['Free', 'Basic', 'Premium', 'Family', 'Business'],
    n_rows,
    p=[0.30, 0.25, 0.20, 0.15, 0.10]
)

# 6. Subscription Prices
price_map = {'Free': 0.00, 'Basic': 9.99, 'Premium': 19.99, 'Family': 29.99, 'Business': 49.99}
subscription_prices = [price_map[plan] for plan in subscription_plans]

# 7. Subscription Type
subscription_types = []
for plan in subscription_plans:
    if plan == 'Free':
        subscription_types.append('N/A')
    else:
        subscription_types.append(np.random.choice(['Monthly', 'Yearly'], p=[0.70, 0.30]))

# 8. Previous Feedback (With Logic Based on Plan)
feedback_options = ['Average', 'Good', 'Awesome', 'Poor', 'Leave to other provider']
feedback_list = []

for plan in subscription_plans:
    if plan == 'Business':
        weights = [0.10, 0.30, 0.45, 0.10, 0.05]  # Business users happier
    elif plan == 'Free':
        weights = [0.20, 0.15, 0.10, 0.35, 0.20]  # Free users complain more
    else:
        weights = [0.25, 0.35, 0.20, 0.15, 0.05]  # Standard distribution
    feedback_list.append(np.random.choice(feedback_options, p=weights))

# 9. Tickets Raised (Correlated with Feedback)
tickets_list = []
for fb in feedback_list:
    if fb == 'Poor':
        tickets_list.append(np.random.choice([3, 4, 5, 6], p=[0.3, 0.3, 0.2, 0.2]))
    elif fb == 'Leave to other provider':
        tickets_list.append(np.random.choice([5, 6, 7, 8], p=[0.25, 0.25, 0.25, 0.25]))
    elif fb == 'Average':
        tickets_list.append(np.random.choice([0, 1, 2], p=[0.4, 0.4, 0.2]))
    elif fb == 'Good':
        tickets_list.append(np.random.choice([0, 1], p=[0.7, 0.3]))
    else:  # Awesome
        tickets_list.append(0)

# 10. Active Status (Influenced by Feedback)
active_status = []
for fb in feedback_list:
    if fb == 'Leave to other provider':
        active_status.append('Inactive')  # Forced Inactive
    elif fb == 'Poor':
        active_status.append(np.random.choice(['Active', 'Inactive'], p=[0.40, 0.60]))
    else:
        active_status.append(np.random.choice(['Active', 'Inactive'], p=[0.90, 0.10]))

# 11. Subscription Start Date
start_date = datetime.now() - timedelta(days=730)
subscription_start_dates = [start_date + timedelta(days=random.randint(0, 730)) for _ in range(n_rows)]

# Create DataFrame
df = pd.DataFrame({
    'User_ID': user_ids,
    'Device_Type': device_types,
    'Location': locations,
    'Auth_Method': auth_methods,
    'Subscription_Plan': subscription_plans,
    'Subscription_Type': subscription_types,
    'Subscription_Price': subscription_prices,
    'Subscription_Start_Date': subscription_start_dates,
    'Tickets_Raised': tickets_list,
    'Previous_Feedback': feedback_list,
    'Active_Status': active_status
})

# Sort by User_ID
df = df.sort_values('User_ID').reset_index(drop=True)

# Save to CSV
df.to_csv('wifi_user_enhanced_data.csv', index=False)

print("✅ Dataset 'wifi_user_enhanced_data.csv' created successfully!")
print(f"📊 Total Rows: {len(df)}")
print("\n📋 Dataset Preview:")
print(df.head(10))
print("\n📈 Feedback Distribution:")
print(df['Previous_Feedback'].value_counts())
print("\n🎫 Average Tickets by Feedback:")
print(df.groupby('Previous_Feedback')['Tickets_Raised'].mean())