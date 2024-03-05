nba api docs:
https://github.com/swar/nba_api/blob/master/README.md


What is a good game?
===============================
BoxScore
	Pace (last 5? meetups)
	Winning/Losing Streaks

Roster
	Ex-Star on Other Teams
	Star Power
	Parity of All-star players on each team
	Avg Roster Age

Schedule
	Last 5? specific meetups
		Results 
		Close game
		Come backs
		OT
		100+ point game

	Last 5? General Games
		Field Goal%

Teams
	Season Record of teams


HARD CODED
	Commentators
	Rivalries
	Loved vs. Hated teams	


============================================================================================

Good Game Score
	Base score of 50
	Each factor adds/subracts points to total


	End Score
		divide GGS by 10 so that it is out of 10
		Above 5 is good
		below 5 is bad
		No lower boundary
			some games can be very shit
	

============================================================================================

Last 5 game results

int calcGameScore(t1, t2)
{
    int GGS
    



    df = lastfivegames(t1, t2)
    use df to calc how many point to add to GGS


    return GGS
}

df lastfivegames(team1, team2)
{
    df lfg
    for i in range(5)
    {
        *api call to get results*
        add results to df

        what df should look like
        # T1 | score 1, score 2...
        # T2 | score 1, score 2...
    }

    return lfg
}

==========================================================




	