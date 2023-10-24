###################################################
# PROJECT: Rating Product & Sorting Reviews in Amazon
###################################################

###################################################
# Business Problem
###################################################

# One of the most important problems in e-commerce is accurately calculating the ratings given to products after sales.
# Solving this problem means providing more customer satisfaction for the e-commerce site, highlighting the product for sellers,
# and ensuring a seamless shopping experience for buyers. Another problem is sorting the reviews given to products correctly,
# misleading reviews coming to the forefront will directly affect the product's sales, causing both financial loss and customer loss.
# Solving these 2 fundamental problems will increase sales for e-commerce sites and sellers, and customers will complete their
# purchasing journey seamlessly.

###################################################
# Data Set Story
###################################################

# This dataset containing Amazon product data includes various metadata along with product categories.
# The product with the most reviews in the Electronics category has user ratings and reviews.

# Variables:
# reviewerID: User ID
# asin: Product ID
# reviewerName: User Name
# helpful: Helpful review rating
# reviewText: Review
# overall: Product rating
# summary: Review summary
# unixReviewTime: Review time
# reviewTime: Review time Raw
# day_diff: Number of days elapsed since the review
# helpful_yes: Number of times the review was found helpful
# total_vote: Number of votes given to the review

###################################################
# TASK 1: Calculate the Weighted Average Rating based on Recent Reviews and Compare it with the Existing Average Rating.
###################################################

# In the shared dataset, users have given ratings and reviews for a product.
# The aim of this task is to evaluate the ratings by weighting them according to the date.
# It is necessary to compare the initial average rating with the weighted rating obtained based on the date.


###################################################
# Step 1: Read the Data Set and Calculate the Average Rating of the Product.
###################################################
import pandas as pd

amazon_rev = pd.read_csv("amazon_review.csv")
avarage_rating = amazon_rev["overall"].mean()
print(avarage_rating)

###################################################
# Step 2: Calculate the Weighted Average Rating Based on the Date.
###################################################
amazon_rev['rev_date'] = pd.to_datetime(amazon_rev['unixReviewTime'], unit='s')
amazon_rev['time_weight'] = (amazon_rev['rev_date'] - amazon_rev['rev_date'].min()).dt.days + 1  # rev time?
w_average = (amazon_rev['time_weight'] * amazon_rev['overall']).sum()
w_average = w_average / amazon_rev['time_weight'].sum()
print(w_average)

###################################################
# TASK 2: Determine the 20 Reviews to be Displayed on the Product Detail Page.
###################################################


###################################################
# Step 1. Generate the helpful_no Variable.
###################################################

# Note:
# total_vote is the total number of up-down votes given to a review.
# up means helpful.
# there is no helpful_no variable in the dataset, it needs to be generated based on existing variables.



###################################################
# Step 2. Calculate score_pos_neg_diff, score_average_rating, and wilson_lower_bound Scores and Add to the Data.
###################################################


##################################################
# Step 3. Determine and Interpret the Top 20 Reviews.
###################################################
