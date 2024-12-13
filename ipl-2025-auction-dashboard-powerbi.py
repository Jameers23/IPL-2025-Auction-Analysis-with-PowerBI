import streamlit as st
import streamlit.components.v1 as components

# Title of the Streamlit app
st.title("IPL 2025 Auction Results and Analysis")

# Sidebar with important information
st.sidebar.title("IPL 2025 Auction Results")
st.sidebar.markdown("""
### Auction Summary (Actual)
- **Date:** November 24 & 25, 2024  
- **Location:** Abadi Al Johar Arena, Jeddah, Saudi Arabia  
- **Players Registered:** 600+  
- **Retained Players:** 46  
- **Total Purse of all Teams:** ₹1200 Crores
- **Purse Spent for Retained Players:** ₹543.25 Crores
- **Auction Pool:** ₹656.75 Crores

### Highest Bid Players (Actual)
1. **Rishabh Pant (LSG)** - ₹27 Crores  
2. **Shreyas Iyer (PBKS)** - ₹26.75 Crores  
3. **Venkatesh Iyer (KKR)** - ₹23.75 Crores  

### Other Interesting Picks
- Arshdeep Singh (PBKS) - ₹18 Crores
- Yuzvendra Chahal (PBKS) - ₹18 Crores
- Ravichandran Ashwin (CSK) - ₹9.75 Crores
- Noor Ahmad (CSK) - ₹10 Crores

### Hot Highlights
- Emerging players from U19 World Cup included.  
- Teams targeted specialist T20 finishers and all-rounders.  
- Dynamic bidding wars witnessed between franchises.  
""")

# Description about IPL 2025
st.markdown("""
The **Indian Premier League (IPL) 2025 Auction** is one of the most anticipated events in cricket.  
Franchises strategize to build their squads with an ideal mix of players for the upcoming season.
Get insights into the auction dynamics, players' performance, and team compositions using the Power BI dashboard below!
""")

# Display an IPL-related image
st.image(
    "https://crictoday.com/wp-content/uploads/2024/07/202401183107287-1.png",
    caption="Indian Premier League",
    use_column_width=True
)

# Add a section for the embedded Power BI iframe
st.subheader("Interactive IPL 2025 Auction Insights")
components.html("""
<iframe title="IPL 2025" width="100%" height="500" src="https://app.powerbi.com/view?r=eyJrIjoiZjVlMzdkNTItMDQ3YS00MDk0LTk4N2ItZGQxZjdiNGQ5NTViIiwidCI6IjRhZDIzNDAxLTliODgtNGQ0ZC04ZmY3LWE5Y2M0OTZkODhiMyJ9" frameborder="0" allowFullScreen="true"></iframe>
""", height=500)

# Section about IPL Auction 2025
st.subheader("Key Takeaways from IPL Auction 2025")
st.markdown("""
- Over 600 players participated in the auction, including established stars and young talents.
- Teams focused on acquiring finishers, all-rounders, and death bowling specialists to build balanced squads.
- Retention strategies and franchise needs significantly influenced bidding wars for certain players.
- Some surprise picks included Noor Ahmad (CSK) and Anshul Kamboj (CSK) for hefty amounts.

**Highest Bids:**
- Rishabh Pant (LSG) - ₹27 Crores (Most Expensive Player in IPL History)
- Shreyas Iyer (PBKS) - ₹26.75 Crores
- Venkatesh Iyer (KKR) - ₹23.75 Crores
""")

# Add another image related to cricket/auction
st.image(
    "https://static.toiimg.com/thumb/msid-115487239,width-1280,height-720,resizemode-4/115487239.jpg",
    caption="Excitement of IPL Auctions",
    use_column_width=True
)

# More about IPL Teams
st.subheader("Teams Participating in IPL 2025")
st.markdown("""
The IPL 2025 will see the participation of the following teams:
1. Chennai Super Kings (CSK)
2. Mumbai Indians (MI)
3. Royal Challengers Bangalore (RCB)
4. Kolkata Knight Riders (KKR)
5. Rajasthan Royals (RR)
6. Delhi Capitals (DC)
7. Punjab Kings (PBKS)
8. Sunrisers Hyderabad (SRH)
9. Lucknow Super Giants (LSG)
10. Gujarat Titans (GT)
""")

# Add an IPL trophy image
st.image(
    "https://akm-img-a-in.tosshub.com/indiatoday/images/story/202409/ipl-trophy-213042235-16x9.jpg?VersionId=n5ubrn4iUMdO6.mKQuZMPSgskfvsLqf8",
    caption="The IPL Trophy",
    use_column_width=True
)

# Footer note
st.markdown("""
Stay tuned for more updates and insights into the IPL 2025 Auction and upcoming season!
""")
