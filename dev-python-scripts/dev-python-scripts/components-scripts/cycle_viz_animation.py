"""MODULE DOCSTRING: Create the animation of a point following
#Json from: https://www.swpc.noaa.gov/products/solar-cycle-progression"""
#Environment: dash1_8_0_env
import pandas as pd     #(version 1.0.0)
import plotly.graph_objects as go
import numpy as np

URL='https://services.swpc.noaa.gov/json/solar-cycle/observed-solar-cycle-indices.json'
df=pd.read_json(URL)



#need to make a moving average of the y (not so smooth movement)
def moving_avg(signal, window_legnth, window_heap):
    """function for moving average"""
    dataOut=[]
    for i in range(0,len(signal),window_heap):
        buffer=signal[i:i+window_legnth]
        dataOut.append(np.mean(buffer))
    return dataOut

WIN_LEN=5
WIN_HEAP=10
#Apply moving average:
y=moving_avg(df.iloc[:,1],WIN_LEN,WIN_HEAP)
N=len(y)
x=np.arange(0,N,1)

xm=np.min(x)-1.5
xM=np.max(x)+1.5
ym=np.min(y)-1.5
yM=np.max(y)+1.5

# s=np.linspace(-1,1,N)#moving point through N=50 positions on the given curve curve
xx=np.arange(0,N,1)
yy=moving_avg(df.iloc[:,1],WIN_LEN,WIN_HEAP)

# Create figure
fig = go.Figure(
    data=[go.Scatter(x=x, y=y,
                     mode="lines",
                     line=dict(width=2, color="blue")),
          go.Scatter(x=x, y=y,
                     mode="lines",
                     line=dict(width=2, color="blue"))],
    layout=go.Layout(
        xaxis=dict(range=[xm, xM], autorange=False, zeroline=False),
        yaxis=dict(range=[ym, yM], autorange=False, zeroline=False),
        title_text="Kinematic Generation of a Planar Curve", hovermode="closest",
        updatemenus=[dict(type="buttons",
                          buttons=[dict(label="Play",
                                        method="animate",
                                        args=[None])])]),
    frames=[go.Frame(
        data=[go.Scatter(
            x=[xx[k]],
            y=[yy[k]],
            mode="markers",
            marker=dict(color="red", size=10))])

        for k in range(N)]
)

fig.show()
"""
the_years = ["1990","1991","1992","1993","1994","1995","1996","1997","1998","1999","2000","2001","2002","2003",
             "2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017"]

df = pd.read_csv("plotly_dash4data\\Gender_StatsData.csv")
df = df[(df["Indicator Name"]=="Expected years of schooling, female")|\
        (df["Indicator Name"]=="Expected years of schooling, male")]
df = df.groupby(["Country Name","Country Code","Indicator Name"], as_index=False)[the_years].mean()
# print(df[:20])


world=["Arab World","South Asia","Latin America & Caribbean","East Asia & Pacific","European Union"]
world_xrange=[4,19]
# asia_latin_years = ["2000","2001","2002","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017"]

# europe=["Bulgaria","Romania","Denmark","France","Hungary"]
# africa=["Malawi","Egypt, Arab Rep.","Mauritania","Morocco","Lesotho"]
# arab=["Jordan","Oman","Qatar","Tunisia","Syrian Arab Republic"]
# asia_central=["India","Iran, Islamic Rep.","Mongolia","Tajikistan","Uzbekistan"]
# latin_caribb=["El Salvador","Mexico","Argentina","Cuba","Chile"]

# europe_xrange=[10,20]
# africa_xrange=[2,15]
# arab_xrange=[6,17]
# asia_central_xrange=[6,16]
# latin_caribb_xrange=[10,19]

# ------------------------------------------------------------------------------
# Choose dataframe Region and sort column
df = df[df['Country Name'].isin(world)]
df['Country Name'] = pd.Categorical(df['Country Name'], ['South Asia','Arab World','East Asia & Pacific',
                                                         'Latin America & Caribbean',"European Union"])
df.sort_values("Country Name", inplace=True)

df = pd.melt(df,id_vars=['Country Name','Country Code','Indicator Name'],var_name='Year',value_name='Rate')
# print(df[:20])


# ------------------------------------------------------------------------------
# Build the dot plot (variation of scatter plot)
fig = px.scatter(df, x="Rate", y="Country Name", color="Indicator Name", animation_frame="Year",
                 range_x=world_xrange, range_y=[-0.5,5.0],
                 title="Gender Gaps in our Education",
                 labels={"Rate":"Years a child is expected to spend at school/university",
                        "Indicator Name":"Gender"} # customize label
      )
fig.update_layout(title={'x':0.5,'xanchor':'center','font':{'size':20}},
                  xaxis=dict(title=dict(font=dict(size=20))),
                  yaxis={'title':{'text':None}},
                  legend={'font':{'size':18},'title':{'font':{'size':18}}})

# print(fig.layout)
# print(fig.data)
# print(fig.frames)

fig.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 800
fig.layout.updatemenus[0].buttons[0].args[1]['transition']['duration'] = 800
fig.data[0].name = 'Girl'
fig.data[1].name = 'Boy'
fig.data[0]['marker'].update(size=14)
fig.data[1]['marker'].update(size=14)
fig.data[0]['marker'].update(color='#22bc22')
fig.data[1]['marker'].update(color="#fda026")

for x in fig.frames:
    x.data[0]['marker']['color'] = '#22bc22'
    x.data[1]['marker']['color'] = '#fda026'

pio.show(fig)
"""