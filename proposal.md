# Birth Control In the US
Katherine Baker, Evelyn Xie, Ella Visconti

# Dataset Records
## Summary:  
The data was gathered from interviews with US adults, studying access, use, impact of COVID-19, relationship, and worries with the change in the Supreme Court in regards to birth control.  

## Search terms and search tool you used to find this dataset
Roper iPoll
October 2020 Birth Control Survey 
URL - (Also be sure to download a local copy)
https://ropercenter.cornell.edu/ipoll/study/31118270
Date Downloaded
18/09/2023 
Authorship
Cornell University, SSRS

## Exact name of the dataset and version
Power to Decide: October 2020 Birth Control Survey  [Roper #31118270]

## Time period, geography, and/or scope covered
October 2020. The US.

## Data formats
Available in CSV, ASCII, Strata, and SPSS Portable file formats. 

## Terms of Use
The dataset can be used as long as it is not being distributed to people outside of Carleton. 

## Suggested Citation if provided
Power to Decide (the National Campaign to Prevent Teen and Unplanned Pregnancy). Power to Decide: October 2020 Birth Control Survey, 2020 [Dataset]. Roper #31118270, Version 3. SSRS [producer]. Cornell University, Ithaca, NY: Roper Center for Public Opinion Research [distributor]. doi:10.25940/ROPER-31118270

## Meaningful Ways User Could Interact and Features:
- Being able to access/look up birth control use by demographics (age, religion, home ownership status, political party, etc.)  

	- Feature: look up use of birth control (col. birt3) based on level of education (col. educ)  
		Usage: python3 birth_control.py –birth-control-by-education “High school graduate (Grade 12 with diploma or GED certificate)”  
		This will return a list of all the reported birth control uses from people with high school as their highest level of education.   
		Function Signature: get_use_of_birth_control(education level)  
			Returns list of birth control usage for that education level
		
	
	- Feature: look up use of birth control (col. BIRT3) based on religion (col. religion)    
		Usage: python3 birth_control.py -- birth-control-by-religion “Catholic”  
		This will return a list of all the reported levels of birth control use from people within the subgroup of their religion.   
		Function Signature: get_use_of_birth_control(religion)
    		Returns list of the use of birth control by people in the specified religion



- Effects of COVID (home ownership status, race, health insurance status, etc. )
People to discuss with (in relation to gender, age, etc.)

	- Feature: look up the availability of individuals to receive in-person sexual and reproductive care as a result of the COVID-19 epidemic (col. birt6a) by the state they are living in (state)
		Usage: python3 birth_control.py –care-after-covid “MN”    
		This will return a list of (mainly) yes’s or no’s - yes means they have been unable to see their provider in person, while no means that  covid has not impacted their ability to see their provider in person.  
		Function Signature: get_care_after_covid(state abbreviation)
			Returns list of whether or not access was available for each pe




- Concerns on Abortion Policy (in relation to political party, religion, etc.)

	- Feature: look up use of birth control (col. BIRT3) based on religion (col. religion)   
		Usage: python3 birth_control.py -- birth-control-by-religion “Catholic”  
		This will return a list of all the reported levels of birth control use from people within the subgroup of their religion.   
		Function Signature: get_use_of_birth_control(religion)
			Returns list of the use of birth control by people in the specified religion




## Team Contract

What are the goals of our team?  
- We want to construct a usable website where users can access information about birth control use and beliefs based on demographics. Some areas we want to focus on are the effects of COVID on birth control use, concerns on abortion policy moving forward from 2020, and which demographics report having someone to confide in regarding sexual and relationship health. Individual goals are as follows:  
	Ella: Learn how to write more organized code in a style that is readable so debugging is much easier than it has been in the past. Ensure everyone is bringing their strengths to the project and maximizing efficiency.   
	Evelyn: Learn more back-end development skills; Cooperate well with teammates, including good communication, reasonable work division, and so on.  
	Katherine: Become more efficient when debugging and coding in general, become more organized in terms of programming and how my code is set up, and develop good communication between team members - I have already worked with Ella and am used to her work style, but I want to get more experience coding with Evelyn and adapting to what she brings to the table.  
    
What are the strengths of our team and its members? 
- Ella: organizing group members into doing a manageable amount of work, some experience with analyzing data, reliable group member in regards to getting work done on time and communicating   
- Evelyn: previous experience with HTML;  willing to communicate with teammates  
- Katherine: Provides consistent, reliable effort; not afraid to ask questions and access resources available to me; communicates regularly and clearly and is flexible with regards to meeting times  

How will we capitalize on the strengths of each member?  
- We will start by having equally-divided roles in terms of coding, organizing the project outside of programming, and communicating. These roles will likely develop over time as we discover our specific strengths within this project, and one person may lean more into one facet of the project.  

What are the rules that will guide your team? Specifically:
When will your team meet? What time, how often, for how long, where?  
- We plan on meeting in Evans and the length of meeting will depend at what point we are at in regards to the work we need to get done and how much has been completed independently.   

What roles will members take on in your meetings? Is someone responsible for setting agendas, taking notes, facilitating discussions, etc?  
- We will start by having relatively equal roles and seeing if anybody leans more towards one certain role. Ella will send the text to decide when we are meeting and if people need a reminder, Katherine will facilitate discussions and bringing our questions to office hours, and Evelyn will work on taking notes in the commit sections of github so we are all on the same page. 

How will you communicate with each other?   
- We will communicate by texting in a group chat.  

How will you make sure communication stays respectful?  
- Responding to another group member’s text as soon as is convenient for you so we are on the same page as often as possible.   

What are the rules for dealing with a teammate who hasn’t been communicating? How frequently should team members communicate / check in?  
- No set rules for how often we should communicate, but if someone reaches out with a question or wants to set up a meeting, both teammates should respond within a few hours. Teammates who are struggling to communicate may need a respectful reminder by other team members.   

What technologies will you use to support team meetings and work?  
- Resources kept via Google Drive	and we prefer to meet in person.  

How will you make decisions?   
- Generally made unanimously or by general consensus. If someone feels especially strongly about one part of the project, we can discuss it further and come to an agreement.   

How will you divide the work?   
- How we divide the work will change once we get started and see who is stronger in certain areas, but at any given time we will have the workload divided as equally as possible for everyone. Katherine will work on the section concerning concerns on abortion policy, Evelyn will do the effects of COVID, and Ella will focus on the different demographics. As we go along, we will divide up our work into different functions and writing the tests for our responsible functions.   

How will you ensure that everybody participates meaningfully? How will you make sure that everyone’s contribution is valued?  
- If we are all treating each other’s ideas, thoughts, and opinions respectfully there should be no issue making sure everyone’s contribution is valued because everyone will be heard in the group and allowed to bring their own ideas to the table.   

What expectations do you have for satisfactory participation? (How much time will each group member spend per week on project activities?)  
- Satisfactory participation means that unless there is an extenuating circumstance or something that you have previously talked to the group about, you will have finished your share of the work by the date we have decided on as a group, so we avoid getting behind or having to scramble to catch up at the end. In regards to the time each week, I would say however long it takes to get your part done within reason (if you are doing some unimaginable amount of work that is affecting your other classes, activities, life it should be brought to the attention of the group and other members can either help or we will go to outside sources for help and advice in how to manage this).  

What process will you follow if someone does not live up to their responsibilities and/or meet the standards for work set by the team?  
- Obviously, sometimes we have rough days or weeks where a lot has come up so we will always approach someone respectfully first and see if there is anything they are stuck on or could use some help with, even if it is just needing more time, but if the problem continues and things are not getting done we would have to bring this to their attention and if the work did not improve we would probably have to make some changes to the group.   

How will you address conflict or deal with disagreements within the team?  
- Top priority is to be respectful and understanding that everyone works differently and has different ideas, and if there is a disagreement it should be discussed as soon as possible to prevent it from becoming a larger issue. 
