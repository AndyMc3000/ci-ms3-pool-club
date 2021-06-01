# Cill na Martra Pool Club (CPC) - Database Schema :floppy_disk: #

## MongoDB Database Collections Schema ## 

The below shows the key:value pairs associated with the MongoDB Collections used for the CPC site. Those Collesctions are; 'league, 'user', and 'matches'.

            league
            {
                _id: ObjectId
                name: String
                description: String
                start_date: Date
                end_date: Date                                                  
                participating_players: Array [        # (this value contains a list of all object id's 
                        ObjectId(user_id),                  in the collection 'user')
                        .....
                        ObjectId(user_id),
                        ] 
            }

            user
            {
                _id: ObjectId
                firstname: String
                lastname: String
                nickname: String
                email: String
                telephone: Integer
                password: String
                admin: Boolean
                rank: Integer
                matches_played: Integer
                matches_won: Integer
                matches_lost: Integer
                games_won: Integer
                games_lost: Integer
                entered_leagues: Array [              # (this value contains a list of all object id's 
                        Object(league_id),                  in the collection 'league')
                        .....
                        Object(league_id)],
                        ]
            }

            matches
            {
                _id: ObjectId
                referee: ObjectId(user_id)
                createdby: ObjectId(user_id)
                playerone: Object(user_id)
                playeronewon: Integer
                playertwo: Object(user_id)
                playertwowon: Integer
                league: Object(league_id)
                date: Date
            }
            
            archive
            {
                _id: ObjectId
                league_name: ObjectId(league_id)
                league_decription: ObjectId(league_id)
                start_date: Object(league_id)
                end_date: Object(league_id)
                participating_players: Array [          # (this value contains a list of all object id's 
                        Object(user_id),                  in the collection 'league')
                        .....
                        Object(league_id)],
                        ]
            }
            
        
