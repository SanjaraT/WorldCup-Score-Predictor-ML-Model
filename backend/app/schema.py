from pydantic import BaseModel, Field
from typing import Literal



class MatchInput(BaseModel):
    batting_team: Literal[
        'Australia',
        'India',
        'Zimbabwe',
        'Bangladesh',
        'New Zealand',
        'South Africa',
        'England',
        'West Indies',
        'Afghanistan',
        'Pakistan',
        'Sri Lanka' 
    ]

    bowling_team: Literal[
        'Australia',
        'India',
        'Zimbabwe',
        'Bangladesh',
        'New Zealand',
        'South Africa',
        'England',
        'West Indies',
        'Afghanistan',
        'Pakistan',
        'Sri Lanka' 
    ]

    city: Literal[
        'Guwahati', 'Brighton', 'Kolkata', 'Rajkot', 'Dubai', 'Bridgetown',
       'Barbados', 'Mirpur', 'Wellington', 'Durban', 'Providence',
       'Christchurch', 'Centurion', 'Canberra', 'East London', 'London',
       'Sharjah', 'Johannesburg', 'Abu Dhabi', 'Gros Islet', 'Karachi',
       'Dambulla', "St George's", 'Colombo', 'Birmingham', 'Cape Town',
       'Cardiff', 'Melbourne', 'Hamilton', 'Delhi', 'Chittagong',
       'Dharamsala', 'Harare', 'Basseterre', 'Mumbai', 'Mount Maunganui',
       'Manchester', 'Hangzhou', 'Brisbane', 'Lauderhill', 'Paarl',
       'Bristol', 'Auckland', 'Taunton', 'Kingston', 'Navi Mumbai',
       'Potchefstroom', 'North Sound', 'Trinidad', 'Dhaka', 'Chelmsford',
       'Sydney', 'Dunedin', 'St Lucia', 'Lahore', 'Chandigarh', 'Lucknow',
       'Sylhet', 'Hambantota', 'Guyana', 'Chennai', 'Southampton',
       'Derby', 'Rawalpindi', 'Kuala Lumpur', 'Chattogram', 'Nagpur',
       'Gqeberha', 'Chester-le-Street', 'Bangalore', 'Hobart', 'Tarouba',
       'Perth', 'Benoni', 'Nelson', 'Nottingham', 'Napier',
       'Thiruvananthapuram', 'Ahmedabad', 'Kandy', 'Northampton',
       'Antigua', 'Carrara', 'Visakhapatnam', 'Pune', 'Adelaide'
    ]

    overs: float = Field(
        ..., 
        gt=0, 
        le=20, 
        description="Overs completed (e.g., 15.2 means 15 overs and 2 balls)"
    )

    wickets: int = Field(
        ..., 
        ge=0, 
        le=10, 
        description="Number of wickets lost so far"
    )

    current_score: int = Field(
        ..., 
        ge=0, 
        description="Current runs"
    )

    last_5_overs_runs: int = Field(
    ..., 
    ge=0, 
    description="Runs scored in the last 5 overs"
    )



class PredictionResponse(BaseModel):
    predicted_score: float = Field(
        ..., 
        description="Predicted final score for the batting team"
    )
    message: str 