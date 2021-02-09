# RandomProjection

In the Bioinformatic Algorithms lesson, we learned how works random projection algorithm. And I decided to make a project about this. In this project my aim is finding motifs using random projection. For more information about random projection, please read Jeremy Buhler and Martin Tompa's "Finding Motifs Using Random Projections" article.

So, I want to show how works my codes.
Firstly, we should get some variables from user. These are DNA, Squence Number and Sequence Length. This program generates a motif length, mutasion number by using this variables. And then, It defines a projection again with these variables.

After that, loop starts. Generate random starting points and save the applicant motifs to a matrix. Then, It checks the applicant motifs are a motif or not. If yes, we got it. Else, try another time.

I want to explain all these with pseudo code and some images.

Program start
	Initialise variables: DNA, Sequence Number, Sequence Length
	Start infinitive loop
		Generate random motif length and tolerance number
		Create bucket matrix with motif length and tolerance number
		Create a projection by call function define_projection with motif 	length and tolerance number
		for i=0: DNA length: Sequence length
			Generate random starting point
			Generate an applicant motif by call function search_motif 		with DNA, start point and projection
			Edit the bucket matrix by call edit_matrix
		end for loop
		Check bucket matrix for applicant motif is best or not by call 	function control_matrix
		if  applicant == Best
			Print motif’s position and motif
      Finish Program
		else
			Reset the bucket matrix
