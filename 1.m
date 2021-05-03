UL = 1000 // upper limit of the number of tosses
a = probability(UL) // Y- axis probability values
b = 1:1:UL // X- axis number of coin flips

// Assumption : 0-> Head , 1-> Tail

plot(b,a) // Plot the graph

function prob = probability(flips) 
    array = [] // to store the calculated probability 
    for index  = 1:flips
        r = randi([0 1],1,index) // generate an sequence of random o->H 1->T for given number of flips
        r = nnz(~r) // calculate the number of heads
        r = r/index // calculate Probability for given number of flips
        array = [array,r]
    end
    prob = array
end



