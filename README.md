# Explainable-AI-for-Multimodal-Credibility-Analysis-of-Online-Beauty-Health-Mis--Information
 - This project proposes an Explainable AI- assisted Multimodal Credibility Assessment System for health blogs hosted online
 that examines the credibility of the platform where the blog is hosted, the credibility of the author of the blog and the credibility of the images that contribute to the blog.
 - This novel framework contributes to the existing body of knowledge by assessing the credibility of misleading beauty blogs using multiple crucial modalities which would lead to
 an insightful information consumption by the users.
 - This proposed pipeline was successfully implemented on multiple carefully curated datasets and correctly identified 274 non credible blogs out of 321 blogs with an accuracy of 97.5%, 
 Precision of 0.973 & F1score of 0.986. Further, the Explainable AI model, with the help of several visualizations displayed the feature contributions for each blog & it's impact and magnitude 
 in a concise comprehensible format.
 - This framework can be further customized and applied to various domains where presence of information is of high concern such as pharmaceutical drug information, pandemic management,
 financial advisories, online healthcare services and cyber frauds. 
 
Methodologies Explored
1) For Web Credibility Analysis : Page Rank Algorithm & Regression Analysis (Web Credibility Score trained on SEO feature scores dataset)
2) For Author Credibility Analysis : Assessing the blog text using CFG Grammar Text, Flesch Reading Ease, Typo Detection, Domain Expertise Test.
3) For Image Credibility Analysis : Transfer Learning for classification & BRISQUE (Blind Reference less Image Spatial Quality Evaluator) for Quality Assessment.
4) Final Model Explanations : SHAPLEY to create our XAI Model with multiple visualization plots. 
