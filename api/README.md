# API server
- API server accepts location and returns JSON response.
- To activate API server, run `python3 apiCall.py`

## API Endpoints

### API Endpoint status
- Endpoint: `http://{serverIP}:5000/api/v1/status`
- Output: `Success`

### News sentiment query
- Endpoint: `http://{serverIP}:5000/api/v1/getNews?location='bengaluru'`
- Output:
```
[
  {
    "documentSentiment": {
      "magnitude": 26.6, 
      "score": 0
    }, 
    "language": "en", 
    "sentences": [
      {
        "sentiment": {
          "magnitude": 0, 
          "score": 0
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "Bengaluru-Seattle direct flight to commence in October."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0, 
          "score": 0
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "American Airlines to connect Bengaluru with Seattle."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0, 
          "score": 0
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "American Airlines announces daily non-stop flight between Bengaluru and Seattle."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0.2, 
          "score": 0.2
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "Bengaluru: American Airlines to operate Bengaluru-Seattle flights daily."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0.1, 
          "score": 0.1
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "Things to do today in Bengaluru."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0.3, 
          "score": 0.3
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "Train tickets booked: Buffalo racer Srinivas Gowda to attend trials at Bengaluru SAI on Monday."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0, 
          "score": 0
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "Karnataka: Mysuru MP, Bengaluru rail activists at loggerheads over Udyan Express extension."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0.6, 
          "score": 0.6
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "Seeking Amits in Bengalurus Kor-mangle."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0.3, 
          "score": 0.3
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "BBMP has fixed Bengaluru traffic problems."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0.2, 
          "score": -0.2
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "Over to beautification now."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0, 
          "score": 0
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "Assam student missing from KIMS hostel in Bengaluru."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0.4, 
          "score": -0.4
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "Return of the billboards in Bengaluru."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0, 
          "score": 0
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "Two Bengaluru brothers have repurposed a motorcycle with a drum kit, an amplifier."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0, 
          "score": 0
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "Bengaluru-Seattle direct flight to begin in October."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0.1, 
          "score": 0.1
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "Bengaluru: Citizen groups urge road agency to save 8,000 trees."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0.2, 
          "score": -0.2
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "Bidar sedition case: Siddaramaiah protests, detained in Bengaluru."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0.8, 
          "score": 0.8
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "An evening of Indian Classical Dance in Bengaluru."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0.6, 
          "score": -0.6
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "Bengaluru: 6.1% jump in job offers at IIMB placements."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0, 
          "score": 0
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "Bangladeshi Hindu refugees in Karnataka move closer to gaining land rights."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0.3, 
          "score": -0.3
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "Imposition of Section 144 in Bengaluru illegal: Karnataka HC."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0.1, 
          "score": 0.1
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "Bengaluru Raptors owner hopeful of host matches at home next year."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0.1, 
          "score": 0.1
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "Karnataka Bandh today, normal life may not be affected in Bengaluru."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0.7, 
          "score": -0.7
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "Bengaluru: Karnataka Bandh call gets tepid response in city."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0, 
          "score": 0
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "Events in Bengaluru on February 15."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0.2, 
          "score": 0.2
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "With cut in funds from centre, Karnatakas debt to increase."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0.1, 
          "score": 0.1
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "Gujarat MLA Jignesh Mevani visits Bengaluru migrant settlements where hutments were razed."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0.2, 
          "score": 0.2
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "Bengaluru civic body to revamp 35 traffic junctions in city."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0.2, 
          "score": 0.2
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "Raja and Rani get married in Bengaluru, theyre horses."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0, 
          "score": 0
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "Twitter reacts."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0.4, 
          "score": -0.4
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "Aspiring Hajis cheated of Rs 1.1 crore by Mumbai-based agents."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0, 
          "score": 0
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "Corona Del Corsa fancied for Bengaluru feature."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0, 
          "score": 0
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "Bengaluru gets another overnight express train to Goa."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0, 
          "score": 0
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "Bengaluru: Lured into flesh trade, Bhojpuri dancer senses trouble, alerts CISF."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0.4, 
          "score": -0.4
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "Bengaluru car crash: Cops shielding Karnataka minister R Ashokas son?."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0, 
          "score": 0
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "Indians from Wuhan not being brought to Bengaluru: Health Department."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0.3, 
          "score": -0.3
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "Bengaluru: 35-year-old man held for selling 30 dummy pistols."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0.7, 
          "score": 0.7
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "Bilal Bagh women have inspired me to speak up: Naseer."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0, 
          "score": 0
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "Hugs for trees: Bengaluru students celebrate Valentine's Day with unique protest."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0, 
          "score": 0
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "Karnataka set to amend Lokayukta Act."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0.1, 
          "score": 0.1
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "Bengaluru: Smart parking will increase footfall, say MG Road traders."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0.2, 
          "score": -0.2
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "Parties publishing candidates criminal cases of little use: Analysts."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0.8, 
          "score": -0.8
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "Watch  Eat Raja, a zero-waste juice shop in Bengaluru."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0.8, 
          "score": -0.8
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "Bengaluru cops bust QR code scam after gang allegedly impersonates citys top cop."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0, 
          "score": 0
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "Karnataka HC gives nod to procure noise meters for Bengaluru."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0, 
          "score": 0
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "Bengaluru: Father sues Amazon, wins new toy for child."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0.2, 
          "score": 0.2
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "Bengaluru: Parkinson's-hit Filipino strums again after 12 years."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0.2, 
          "score": -0.2
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "Firearms recovered, 2 arrested in Bengaluru."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0, 
          "score": 0
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "Bengaluru: Smuggling kingpin who slipped in gold worth Rs 70 crore nabbed at KIA."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0.1, 
          "score": -0.1
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "Bengaluru: Fire breaks out at hotel in Kormangala, one critical out of 11."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0, 
          "score": 0
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "Tales of Malgudi come to namma Bengaluru."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0.1, 
          "score": -0.1
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "Sports tech start-ups ride tennis wave at Bengaluru Open 2020."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0, 
          "score": 0
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "Land dispute leaves 30 families homeless in Bengaluru."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0.4, 
          "score": -0.4
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "Watch: Bengaluru Businessman Crashes Lamborghini Into Traffic Post."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0.1, 
          "score": 0.1
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "A fusion music fest in Bengaluru."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0, 
          "score": 0
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "Lamborghini rams traffic police chowki in Bengaluru."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0, 
          "score": 0
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "Bengaluru key to Goldman's consumer bank Marcus."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0, 
          "score": 0
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "Bengaluru: 32 sheds of migrants razed in Munekolalu."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0.7, 
          "score": -0.7
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "The Daily Fix: Bengaluru is making protest the privilege of the rich by demanding costly sureties."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0, 
          "score": 0
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "Leander Paes-Matthew Ebden go one step closer to Bengaluru Open title."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0.2, 
          "score": 0.2
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "At Bengalurus Bilal Bagh, support pours in for Jamia Millia Islamia students."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0, 
          "score": 0
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "Is carrying meat in Bengaluru's Namma Metro prohibited BMRCL clarifies list of restricted goods."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0.2, 
          "score": 0.2
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "4.6L cases booked in 10 months for ticketless travel in Bengaluru Railway Division."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0.1, 
          "score": 0.1
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "250 Odia Labourers Rescued From Bengaluru."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0, 
          "score": 0
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "Sitharaman To Visit Hyderabad, Bengaluru To Hold Interactive Sessions On Budget 2020-21."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0.7, 
          "score": 0.7
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "Wedding of horse couple performed to celebrate Valentine's Day in Bengaluru."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0.1, 
          "score": -0.1
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "Karnataka bandh today: What is happening in Bengaluru, Mangaluru, and other cities?."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0, 
          "score": 0
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "Karnataka gets nod for three more airports."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0.1, 
          "score": -0.1
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "Bengaluru Congress MLA's Son, Out On Bail, Denies Role In Bentley Crash."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0, 
          "score": 0
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "Karnataka's new Urban Development minister announces Rs 200 crore flyover in Bengaluru."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0, 
          "score": 0
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "Bengaluru: City police on high alert for bandh."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0.8, 
          "score": -0.8
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "Bengaluru: Man burnt alive in abandoned car."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0.2, 
          "score": 0.2
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "After Delhi win, AAP eyes mission Bengaluru', looks to repeat success in BBMP polls."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0, 
          "score": 0
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "Bengaluru: Mohammed Nalapad Haris held, released on bail in Bentley accident case."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0.1, 
          "score": 0.1
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "Coronavirus outbreak: Police urged to suspend use of breathalysers in Bengaluru."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0, 
          "score": 0
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "Bengaluru: IPS officer stages sit-in outside home of ex-wife, also an IPS."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0.1, 
          "score": 0.1
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "Namma Bengaluru app launched for all civic plaints."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0.4, 
          "score": 0.4
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "Infidelity capital: Bengaluru sees rise in murders over love."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0.9, 
          "score": 0.9
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "Bengaluru: New halt railway station to ease KIA staffs commuting woes."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0.2, 
          "score": 0.2
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "Bengaluru minister pays surprise visit to Indira Gandhi hospital, gets shocked with state of affairs."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0.4, 
          "score": -0.4
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "Karnataka: Two police teams to probe Mercedes crash near Ballari."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0.5, 
          "score": -0.5
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "Bengaluru Businessman Crashes Lamborghini Into Traffic Post, Posts Pics."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0, 
          "score": 0
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "Nutanix officially commissions new India headquarters in Bengaluru."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0, 
          "score": 0
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "Bengaluru will be the latest city to get its own suburban rail network."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0.8, 
          "score": -0.8
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "Bengaluru techie falls prey to online fraud twice, loses Rs 37 lakh; wife walks out of marriage with chil."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0, 
          "score": 0
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "Bengaluru: Protesting blind students detained, released later."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0, 
          "score": 0
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "Speeding car kills cop checking rash driving in Bengaluru."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0.3, 
          "score": 0.3
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "Blood donation marks V-Day in Bengaluru college."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0, 
          "score": 0
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "IPL 2020: Virat Kohli-led Royal Challengers Bangalore to be renamed as Royal Challengers Bengaluru?."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0, 
          "score": 0
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "India's singles challenge ends at Bengaluru Open but Paes marches into semis with doubles partner Abden."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0.6, 
          "score": -0.6
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "Two more seeds crash at Bengaluru Open."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0.3, 
          "score": 0.3
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "Two techies drown in Bengaluru's Kalkere lake."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0.9, 
          "score": -0.9
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "Vodafone Idea blames fibrecut for Bengaluru network outage."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0.5, 
          "score": 0.5
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "I was blessed: Bengaluru musician travels 61,000 km to meet families of 40 killed in Pulwama."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0.3, 
          "score": -0.3
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "Silk Board will live up to its infamous reputation as Bengalurus worst traffic nightmare; here's how."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0.6, 
          "score": -0.6
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "Bengaluru: Cops foil anti-CAA protest in Shivajinagar."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0.4, 
          "score": 0.4
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "KSRTCs most frequent passenger made 148 Bengaluru-Ernakulam trips last year."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0, 
          "score": 0
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "Bengaluru's story: 96.21L in 2011, 1.42 cr by 2021."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0, 
          "score": 0
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "Two more seeds fall in gruelling 3-setters of Bengaluru Open."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0.1, 
          "score": -0.1
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "Bengaluru: You may not get Ola, Uber cabs on Feb 13."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0.5, 
          "score": 0.5
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "Bengaluru woman suspects fidelity, pours boiling oil on sleeping hubby."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0, 
          "score": 0
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "Bengaluru: JD(S) spreading rumours concerning my portfolio - Min Narayana Gowda."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0.4, 
          "score": -0.4
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "Bengaluru: HPCL holds Saksham campaign in KR Pura."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0.1, 
          "score": 0.1
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "Shaheen Bagh comes to Bengalurus Bilal Bagh."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0.5, 
          "score": -0.5
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "In Bengaluru, eating out to get costlier."
        }
      }, 
      {
        "sentiment": {
          "magnitude": 0.3, 
          "score": 0.3
        }, 
        "text": {
          "beginOffset": -1, 
          "content": "Bengaluru all set to witness a musical."
        }
      }
    ]
  }
]
```