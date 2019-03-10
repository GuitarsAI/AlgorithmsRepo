// Function Convolution1D
function Convolution1D(f,g,delay=false)
{
        
        // Define output matrix with zeros
        var y = new Array(f.length+g.length-1).fill(0);
        
        // Convolution
        for (n=0;n<f.length;++n)
        {
            for(m=0;m<g.length;++m)
            {
                
                y[m+n]+=f[n]*g[m];
            }
        }
        if(delay)
        {
              return y.slice(Math.round((g.length-1)/2),-g.length);
        }
	else
	{return y;}
}

module.exports.Convolution1D = Convolution1D;
