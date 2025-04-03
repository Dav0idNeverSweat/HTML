import sqlite3

conn = sqlite3.connect('Temp/quiz.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS TOPIC (
               ID INT,
               Topic CHAR(30),
               PRIMARY KEY (ID, Topic) 
               )
''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS QUESTION (
               ID INT,
               "TOPIC ID" INT,
               Question CHAR(255),
               PRIMARY KEY(ID,"TOPIC ID"),
               FOREIGN KEY("TOPIC ID") REFERENCES TOPIC(ID)
               )
''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS ANSWER (
               ID INT,
               "QUESTION ID" INT,
                "Correct" CHAR(255),
                "Incorrect1" CHAR(255),
               "Incorrect2" CHAR(255),
               "Incorrect3" CHAR(255),
               PRIMARY KEY(ID,"QUESTION ID"),
               FOREIGN KEY("QUESTION ID") REFERENCES QUESTION(ID)
               )
''')



# KILL TABLE #
# cursor.execute('''
#     DROP TABLE ANSWER
# ''')

# Table TOPIC #
# cursor.execute('''INSERT INTO Topic(ID, Topic) VALUES(1, "Technology")''')
# cursor.execute('''INSERT INTO Topic(ID, Topic) VALUES(2, "Math")''')
# cursor.execute('''INSERT INTO Topic(ID, Topic) VALUES(3, "Science")''')

#### Table QUESTION[Question(ID, TOPIC ID, Question)] ####
### Structure: ID|Topic ID|Question ###
## Science[ID:1->3|Topic ID:3] ##

# 1|3|How do genetic mutations contribute to the process of evolution? # done
# cursor.execute('''INSERT INTO QUESTION(ID, "TOPIC ID", Question) VALUES(1, 3, "How do genetic mutations contribute to the process of evolution?")''')

# 2|3|What are the potential consequences of melting permafrost on global climate patterns? #
# cursor.execute('''INSERT INTO QUESTION(ID, "TOPIC ID", Question) VALUES(2, 3, "What are the potential consequences of melting permafrost on global climate patterns?")''')
# # 3|3|How does quantum entanglement challenge our traditional understanding of physics? #
# cursor.execute('''INSERT INTO QUESTION(ID, "TOPIC ID", Question) VALUES(3, 3, "How does quantum entanglement challenge our traditional understanding of physics?")''')
# ## Mathematics[ID:4->6|Topic ID:2] ##
# # 4|2|How does the Fibonacci sequence appear in nature and architecture? #
# cursor.execute('''INSERT INTO QUESTION(ID, "TOPIC ID", Question) VALUES(4, 2, "How does the Fibonacci sequence appear in nature and architecture?")''')
# # 5|2|What is the significance of prime numbers in cryptography? #
# cursor.execute('''INSERT INTO QUESTION(ID, "TOPIC ID", Question) VALUES(5, 2, "What is the significance of prime numbers in cryptography?")''')
# # 6|2|How can calculus be applied to model real-world phenomena such as population growth? #
# cursor.execute('''INSERT INTO QUESTION(ID, "TOPIC ID", Question) VALUES(6, 2, "How can calculus be applied to model real-world phenomena such as population growth?")''')
# ## Technology[ID:7->9|Topic ID:1] ##
# # 7|1|What are the ethical implications of using AI in surveillance systems? #
# cursor.execute('''INSERT INTO QUESTION(ID, "TOPIC ID", Question) VALUES(7, 1, "What are the ethical implications of using AI in surveillance systems?")''')
# # 8|1|How can blockchain technology enhance data security and privacy? #
# cursor.execute('''INSERT INTO QUESTION(ID, "TOPIC ID", Question) VALUES(8, 1, "How can blockchain technology enhance data security and privacy?")''')
# # 9|1|What are the limitations of current battery technologies in electric vehicles? #
# cursor.execute('''INSERT INTO QUESTION(ID, "TOPIC ID", Question) VALUES(9, 1, "What are the limitations of current battery technologies in electric vehicles?")''')

# ### Table ANSWER ###
# ## Structure: ID|Question ID|Correct|Incorrect1|Incorrect2|Incorrect3 ##

# # # 1/1 Science
# # 1|1|...(Correct)|...(Incorrect1)|...(Incorrect2)|...(Incorrect3)
# # cursor.execute('''INSERT INTO ANSWER(ID, "QUESTION ID", Correct, Incorrect1, Incorrect2, Incorrect3) 
# #                VALUES(1, 1, "They introduce genetic diversity, which natural selection can act upon to drive evolution.", "They always cause harmful effects that hinder evolution.", "Mutations are reversed by DNA repair mechanisms, preventing evolution.", "Evolution only occurs through acquired traits, not genetic mutations.")
# #                ''')
# #2/2 Science
# cursor.execute('''INSERT INTO ANSWER(ID, "QUESTION ID", Correct, Incorrect1, Incorrect2, Incorrect3) 
#                VALUES(2, 2, "It can release large amounts of methane, a potent greenhouse gas, accelerating climate change.", "It cools the atmosphere by absorbing carbon dioxide.", "It has no significant impact since methane is quickly neutralized.", "It enhances soil fertility without environmental risks.")
#                ''')
# #3/3 Science
# cursor.execute('''INSERT INTO ANSWER(ID, "QUESTION ID", Correct, Incorrect1, Incorrect2, Incorrect3) 
#                VALUES(3, 3, "It suggests that particles can instantaneously affect each other regardless of distance, contradicting classical locality.", "It proves that information can travel faster than light.", "It demonstrates that particles can exist in multiple places at once.", "It eliminates the need for the uncertainty principle in quantum mechanics.")
#                ''')
# #4/4 Mathematics
# cursor.execute('''INSERT INTO ANSWER(ID, "QUESTION ID", Correct, Incorrect1, Incorrect2, Incorrect3) 
#                VALUES(4, 4, "It is seen in patterns like the arrangement of leaves, pine cones, and the Parthenon's proportions.", "It only exists in abstract mathematics, not in real-world patterns.", "It is a random sequence with no structural significance.", "It dictates the growth of all organisms without exception.")
#                ''')
# #5/5 Mathematics
# cursor.execute('''INSERT INTO ANSWER(ID, "QUESTION ID", Correct, Incorrect1, Incorrect2, Incorrect3) 
#                VALUES(5, 5, "They form the basis of encryption algorithms like RSA, providing security through factorization difficulty.", "They are used to compress data by eliminating redundant bits.", "They simplify encryption by allowing easy factorization.", "Prime numbers ensure encryption keys never change.")
#                ''')
# #6/6 Mathematics
# cursor.execute('''INSERT INTO ANSWER(ID, "QUESTION ID", Correct, Incorrect1, Incorrect2, Incorrect3) 
#                VALUES(6, 6, "Differential equations can describe the rate of change in population size over time.", "Calculus can only be applied to static, unchanging systems.", "It is used to approximate discrete population counts directly.", "Calculus eliminates the need for statistical analysis in growth models.")
#                ''')
# #7/7 Technology
# cursor.execute('''INSERT INTO ANSWER(ID, "QUESTION ID", Correct, Incorrect1, Incorrect2, Incorrect3) 
#                VALUES(7, 7, "It raises concerns about privacy, bias, and potential misuse by authorities.", "It eliminates bias entirely, ensuring fair surveillance.", "It guarantees privacy protection through encryption alone.", "AI is only used for beneficial purposes, making ethical concerns irrelevant.")
#                ''')
# #8/8 Technology
# cursor.execute('''INSERT INTO ANSWER(ID, "QUESTION ID", Correct, Incorrect1, Incorrect2, Incorrect3) 
#                VALUES(8, 8, "It uses cryptographic techniques to secure data and prevent unauthorized modifications.", "It relies solely on centralized servers for data security.", "It encrypts data using reversible public keys only.", "It replaces cryptography with hashing for security.")
#                ''')
# #9/9 Technology
# cursor.execute('''INSERT INTO ANSWER(ID, "QUESTION ID", Correct, Incorrect1, Incorrect2, Incorrect3) 
#                VALUES(9, 9, "Limited energy density and long charging times are significant challenges.", "Batteries have unlimited lifespan and efficiency.", "They can be charged instantly without energy loss.", "Weight and size have no impact on vehicle range.")
#                ''')



# Kill Table Element(FROM Topic) Base on ID(ID = 1) #
# cursor.execute('''
#     DELETE FROM Topic WHERE ID = 1;
# ''')

conn.commit() # Update db
conn.close() # close connection