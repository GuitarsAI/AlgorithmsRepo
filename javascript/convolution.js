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
};

module.exports.Convolution1D = Convolution1D;

function Convolution2D(f,g)
{
        // Define output matrix with zeros
        var result = [];
        for ( var i = 0; i<(f.length+g.length-1);++i)
        {
            result[i]=[];
            for (var j = 0 ; j < (f[0].length+g[0].length-1);++j)
            {
             result[i][j]=0;
            }
        }
        
        
        // Convolution
        for (x=0;x<f.length;++x)
        {
            for(y=0;y<f[0].length;++y)
            {
                for(i=0;i<g.length;++i)
                {
                    for (j=0;j<g[0].length;++j)
                    {
                        result[x+i][y+j]+=f[x][y]*g[i][j];
                    }
                }
            }
        }
        
        return result;
      
}

module.exports.Convolution2D = Convolution2D;
