# Cill na Martra Pool Club (CPC) - Database Schema :floppy_disk: #

## MongoDB Database Collections Schema ## 

The below shows the key:value pairs associated with the MongoDB Collections used for the CPC site. Those Collesctions are; 'league, 'user', and 'matches'.

            league
            {
                _id:
                name:
                description:
                start_date:
                end_date:
                participating_players: [ObjectId(user_id),..ObjectId(user_id)] (list of all object id's in collection 'user')
            }

            user
            {
                _id:
                firstname:
                lastname:
                nickname:
                email:
                telephone:
                password:
                admin:
                rank:
                matches_played:
                matches_won:
                matches_lost:
                games_won:
                games_lost:
                entered_leagues: [Object(league_id),..Object(league_id)] (list of object id's of the leagues)
            }

            matches
            {
                _id
                referee:
                createdby:
                playerone: Object(_id)
                playeronewon:
                playertwo: Object(_id)
                playertwowon:
                league: Object(_id)
                date:
            }
