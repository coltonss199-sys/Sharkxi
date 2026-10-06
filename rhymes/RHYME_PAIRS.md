# Rhyme Pairs That Mean Something

1000 two-syllable rhyme pairs where the sound link reinforces a meaning link, mined from the [CMU Pronouncing Dictionary](https://github.com/cmusphinx/cmudict) — 100 per vowel, one search agent per long and short vowel.

**Every pair was machine-checked against CMU** (`validate.py`):

- both words are two syllables in every CMU pronunciation (so no cov-ring / co-ver-ing ambiguity), labelled **iamb** (da-DUM) or **trochee** (DUM-da) exactly as CMU stresses them;
- no r- or l-controlled syllables: no ER, no vowel closed by R or L, no syllabic -le, no silent-L spelling (talk, calm), no suffixed base-final L (roll-ing, feel-ing), and no vowel letter closed by R in the spelling (sur-prise);
- the rhyme type is the one CMU's phonemes actually support — **perfect** (identical from the stressed vowel on), **slant** (one or two near-consonant swaps, or a different vowel over identical endings), or **assonance** (same stressed vowel only).

Meaning links, positivity, and ranking (strongest sound + sense first) are editorial judgments by the agents. Each section ends with five near-misses that were rejected.

| Vowel | Pairs | Perfect | Slant | Assonance |
|---|---|---|---|---|
| [Long A /eɪ/](#long-a) | 100 | 44 | 24 | 32 |
| [Long E /iː/](#long-e) | 100 | 44 | 32 | 24 |
| [Long I /aɪ/](#long-i) | 100 | 32 | 25 | 43 |
| [Long O /oʊ/](#long-o) | 100 | 34 | 32 | 34 |
| [Long U /uː/, /juː/](#long-u) | 100 | 23 | 33 | 44 |
| [Short A /æ/](#short-a) | 100 | 34 | 24 | 42 |
| [Short E /ɛ/](#short-e) | 100 | 39 | 38 | 23 |
| [Short I /ɪ/](#short-i) | 100 | 34 | 31 | 35 |
| [Short O /ɑ/, /ɔ/](#short-o) | 100 | 17 | 55 | 28 |
| [Short U /ʌ/](#short-u) | 100 | 18 | 47 | 35 |

## Long A

/eɪ/ as in *brave, grateful* — CMU `EY` under primary stress.

| # | Pair | Rhyme type | Relationship | One-line example use |
|---|---|---|---|---|
| 1 | **places** (trochee) / **spaces** (trochee) | perfect | synonyms: open room to roam | We'll find new places, wide-open spaces, you and me |
| 2 | **racing** (trochee) / **chasing** (trochee) | perfect | synonyms: running after dreams | Racing through the meadow, chasing fireflies at dusk |
| 3 | **ages** (trochee) / **stages** (trochee) | perfect | synonyms: phases of life | Through all the ages and the stages, I'll hold on |
| 4 | **waning** (trochee) / **gaining** (trochee) | perfect | antonyms: shrinking versus growing | The winter's waning and the light is gaining ground |
| 5 | **display** (iamb) / **array** (iamb) | perfect | synonyms: bright showcase of colors | A bright display, a dazzling array of lights |
| 6 | **create** (iamb) / **innate** (iamb) | perfect | antonyms: made versus inborn | Some gifts are innate, the rest we create |
| 7 | **sustain** (iamb) / **remain** (iamb) | perfect | synonyms: lasting and enduring | Let the music sustain, let the melody remain |
| 8 | **domain** (iamb) / **terrain** (iamb) | perfect | synonyms: land and territory | This green domain, this rolling, wild terrain |
| 9 | **fated** (trochee) / **slated** (trochee) | perfect | synonyms: destined to happen | We were fated, slated for a sunny ending |
| 10 | **contain** (iamb) / **restrain** (iamb) | perfect | synonyms: holding feelings in | I can't contain this joy, can't restrain this smile |
| 11 | **faded** (trochee) / **shaded** (trochee) | perfect | synonyms: softened, muted colors | Faded denim, shaded porches in July |
| 12 | **refrain** (iamb) / **abstain** (iamb) | perfect | synonyms: gently holding back | Let's refrain from rushing and abstain from all the noise |
| 13 | **upgrade** (iamb) / **remade** (iamb) | perfect | synonyms: improved and renewed | A total upgrade, our little home remade |
| 14 | **conveyed** (iamb) / **displayed** (iamb) | perfect | synonyms: shown and expressed | The love she conveyed was displayed in her eyes |
| 15 | **equate** (iamb) / **relate** (iamb) | perfect | synonyms: connect and compare | Nothing could equate to the way our hearts relate |
| 16 | **training** (trochee) / **gaining** (trochee) | perfect | cause/effect: practice builds strength | Every morning training, every day I'm gaining |
| 17 | **amaze** (iamb) / **displays** (iamb) | perfect | cause/effect: dazzling shows bring wonder | Fireworks light the night, and the bright displays amaze |
| 18 | **lazy** (trochee) / **hazy** (trochee) | perfect | same scene: slow summer afternoon | A lazy, hazy afternoon beneath the willow |
| 19 | **lazy** (trochee) / **daisy** (trochee) | perfect | same scene: summer meadow nap | Lying lazy in the daisy field all afternoon |
| 20 | **gazing** (trochee) / **grazing** (trochee) | perfect | same scene: quiet country meadow | Gazing at the horses grazing in the clover |
| 21 | **raising** (trochee) / **praising** (trochee) | perfect | same scene: voices lifted high | Raising up our voices, praising every dawn |
| 22 | **playing** (trochee) / **swaying** (trochee) | perfect | same scene: music and dancing | The band is playing and the crowd is swaying |
| 23 | **latest** (trochee) / **greatest** (trochee) | perfect | same domain: newest, finest things | Here's my latest and my greatest love song |
| 24 | **gracious** (trochee) / **spacious** (trochee) | perfect | same scene: welcoming open home | A gracious host inside a spacious sunny hall |
| 25 | **phrases** (trochee) / **praises** (trochee) | perfect | same domain: words of song | Singing phrases full of praises to the sky |
| 26 | **rainy** (trochee) / **sunny** (trochee) | slant | antonyms: wet versus bright | Rainy mornings turn to sunny afternoons |
| 27 | **lazy** (trochee) / **easy** (trochee) | slant | synonyms: relaxed and slow | Lazy Sunday morning, easy as a breeze |
| 28 | **embrace** (iamb) / **release** (iamb) | slant | antonyms: hold versus let go | Embrace the moment, then release your fears |
| 29 | **staying** (trochee) / **going** (trochee) | slant | antonyms: stay versus leave | Whether you're staying or going, you are loved |
| 30 | **acclaim** (iamb) / **esteem** (iamb) | slant | synonyms: praise and respect | They earned acclaim and the esteem of every friend |
| 31 | **painted** (trochee) / **tinted** (trochee) | slant | synonyms: colored with hue | Painted skies and tinted window light |
| 32 | **amaze** (iamb) / **amuse** (iamb) | slant | synonyms: delight and entertain | Tricks that amaze and jokes that amuse |
| 33 | **bravely** (trochee) / **safely** (trochee) | slant | antonyms: bold versus careful | Go forth bravely, then come home safely |
| 34 | **making** (trochee) / **baking** (trochee) | perfect | same scene: warm kitchen treats | We're making memories and baking bread at home |
| 35 | **ballet** (iamb) / **bouquet** (iamb) | perfect | same scene: dance recital flowers | After the ballet she held a rose bouquet |
| 36 | **spraying** (trochee) / **swaying** (trochee) | perfect | same scene: breezy beach day | Ocean mist is spraying and the palms are swaying |
| 37 | **daisy** (trochee) / **hazy** (trochee) | perfect | same scene: summer meadow | A daisy chain on a hazy afternoon |
| 38 | **hooray** (iamb) / **today** (iamb) | perfect | same scene: celebration day | Shout hooray, it's our big day today |
| 39 | **praying** (trochee) / **saying** (trochee) | perfect | same domain: words of thanks | Praying softly, saying thanks for every sunrise |
| 40 | **cafe** (iamb) / **buffet** (iamb) | perfect | same scene: sunny brunch outing | Brunch at the cafe, a sunny buffet |
| 41 | **cafe** (iamb) / **chalet** (iamb) | perfect | same scene: snowy alpine village | Cocoa at the cafe, then home to our chalet |
| 42 | **erase** (iamb) / **replace** (iamb) | perfect | cause/effect: clear then renew | Erase the gray and replace it with gold |
| 43 | **aiming** (trochee) / **framing** (trochee) | perfect | same domain: taking a photo | Aiming at the sunset, framing it just right |
| 44 | **blazing** (trochee) / **gazing** (trochee) | perfect | same scene: campfire night | Gazing at the blazing campfire light |
| 45 | **races** (trochee) / **paces** (trochee) | perfect | same domain: running track | We ran the races, put our hearts through paces |
| 46 | **plated** (trochee) / **grated** (trochee) | perfect | same domain: preparing dinner | Cheese grated fresh and plated with a smile |
| 47 | **engage** (iamb) / **onstage** (iamb) | perfect | same scene: performer and crowd | Step onstage and engage the crowd tonight |
| 48 | **pages** (trochee) / **stages** (trochee) | perfect | same domain: stories and theater | Turning pages, setting stages for our tale |
| 49 | **parade** (iamb) / **cascade** (iamb) | perfect | same scene: festive confetti shower | A cascade of confetti fell on the parade |
| 50 | **faces** (trochee) / **graces** (trochee) | perfect | same domain: charm and beauty | Smiling faces full of little graces |
| 51 | **navy** (trochee) / **wavy** (trochee) | perfect | same scene: deep ocean water | Navy water, wavy lines along the shore |
| 52 | **waking** (trochee) / **baking** (trochee) | perfect | same scene: early morning kitchen | Waking up to the smell of Mama baking |
| 53 | **skating** (trochee) / **floating** (trochee) | slant | synonyms: smooth gliding motion | Skating so smooth it feels like floating |
| 54 | **saying** (trochee) / **showing** (trochee) | slant | synonyms: expressing your heart | Saying it is easy, showing takes your heart |
| 55 | **baby** (trochee) / **lady** (trochee) | slant | same domain: girl growing up | My baby girl grew up into a graceful lady |
| 56 | **swaying** (trochee) / **blowing** (trochee) | slant | cause/effect: wind moves trees | Trees are swaying while the wind is blowing |
| 57 | **attain** (iamb) / **acclaim** (iamb) | slant | cause/effect: success earns praise | Dream high, attain it, and bask in the acclaim |
| 58 | **hazy** (trochee) / **breezy** (trochee) | slant | same scene: summer evening | Hazy skies and breezy summer nights |
| 59 | **champagne** (iamb) / **balloon** (iamb) | slant | same scene: party celebration | Pop the champagne, let loose the balloon |
| 60 | **tasty** (trochee) / **crusty** (trochee) | slant | same scene: fresh warm bread | Tasty loaves with crusty golden tops |
| 61 | **champagne** (iamb) / **cuisine** (iamb) | slant | same domain: fine dining | Chilled champagne and fine French cuisine |
| 62 | **gazing** (trochee) / **rising** (trochee) | slant | same scene: watching sunrise | Gazing at the rising sun above the hill |
| 63 | **skating** (trochee) / **boating** (trochee) | slant | same domain: lake recreation | Skating in December, boating in July |
| 64 | **painting** (trochee) / **printing** (trochee) | slant | same domain: making art | Painting canvases and printing posters bright |
| 65 | **playing** (trochee) / **growing** (trochee) | slant | same scene: happy childhood | Children playing, growing taller every day |
| 66 | **terrain** (iamb) / **ravine** (iamb) | slant | same domain: rugged landscape | Across the green terrain and down the deep ravine |
| 67 | **tasting** (trochee) / **roasting** (trochee) | slant | same scene: summer cookout | Roasting corn and tasting summer on the grill |
| 68 | **saving** (trochee) / **giving** (trochee) | slant | same domain: generous money habits | Saving up and giving back with love |
| 69 | **remain** (iamb) / **staying** (trochee) | assonance | synonyms: stay right here | I'll remain here, staying by your side |
| 70 | **create** (iamb) / **making** (trochee) | assonance | synonyms: building something new | Let's create a song, making something new |
| 71 | **explain** (iamb) / **convey** (iamb) | assonance | synonyms: put into words | I can't explain or convey how much I care |
| 72 | **behave** (iamb) / **obey** (iamb) | assonance | synonyms: follow the rules | Behave yourself and obey the golden rule |
| 73 | **escape** (iamb) / **away** (iamb) | assonance | synonyms: breaking free | Let's escape the city, slip away tonight |
| 74 | **safety** (trochee) / **haven** (trochee) | assonance | synonyms: shelter and protection | In the safety of this quiet haven |
| 75 | **famous** (trochee) / **nameless** (trochee) | assonance | antonyms: known versus unknown | Famous or nameless, I'll love you the same |
| 76 | **making** (trochee) / **shaping** (trochee) | assonance | synonyms: forming something new | Making clay and shaping dreams by hand |
| 77 | **maiden** (trochee) / **lady** (trochee) | assonance | synonyms: fair young woman | A gentle lady, once a village maiden |
| 78 | **obtain** (iamb) / **gaining** (trochee) | assonance | synonyms: acquiring something | Gaining ground to obtain the golden prize |
| 79 | **dainty** (trochee) / **lacy** (trochee) | assonance | synonyms: delicate and fine | A dainty dress with lacy sleeves |
| 80 | **gracious** (trochee) / **patient** (trochee) | assonance | synonyms: kind, gentle virtues | Be gracious, be patient, be kind |
| 81 | **stately** (trochee) / **gracious** (trochee) | assonance | synonyms: dignified and elegant | A stately bow, a gracious smile |
| 82 | **domain** (iamb) / **estate** (iamb) | assonance | synonyms: owned land | Our small domain, this cozy country estate |
| 83 | **await** (iamb) / **patience** (trochee) | assonance | synonyms: patient anticipation | I await you with patience and a smile |
| 84 | **patience** (trochee) / **waiting** (trochee) | assonance | cause/effect: patience eases waiting | Patience is the gift of waiting well |
| 85 | **awake** (iamb) / **daybreak** (trochee) | assonance | same scene: early morning | I'm wide awake at daybreak, full of hope |
| 86 | **rainbow** (trochee) / **cascade** (iamb) | assonance | same scene: misty waterfall | A rainbow shimmers in the cascade spray |
| 87 | **daisy** (trochee) / **bouquet** (iamb) | assonance | part/whole: flower in bunch | A single daisy tucked in her bouquet |
| 88 | **fragrance** (trochee) / **bouquet** (iamb) | assonance | same scene: fresh flowers | The fragrance of a springtime bouquet |
| 89 | **rainbow** (trochee) / **halo** (trochee) | assonance | same scene: arcs of light | A rainbow halo circling the moon |
| 90 | **baking** (trochee) / **pastry** (trochee) | assonance | same scene: morning bakery | Baking pastry in the morning light |
| 91 | **rainbow** (trochee) / **painted** (trochee) | assonance | same scene: colorful sky | A rainbow painted on the evening sky |
| 92 | **sacred** (trochee) / **haven** (trochee) | assonance | same domain: peaceful sanctuary | We found a sacred haven by the sea |
| 93 | **ancient** (trochee) / **ages** (trochee) | assonance | same domain: deep history | Ancient songs that echo through the ages |
| 94 | **shading** (trochee) / **tracing** (trochee) | assonance | same domain: careful drawing | Tracing gentle lines and shading in the light |
| 95 | **ballet** (iamb) / **dainty** (trochee) | assonance | same scene: graceful dancer | Dainty steps across the ballet stage |
| 96 | **skating** (trochee) / **lakeside** (trochee) | assonance | same scene: frozen winter lake | Skating by the lakeside under winter stars |
| 97 | **famous** (trochee) / **acclaim** (iamb) | assonance | same domain: fame and praise | Famous for your kindness, rich in acclaim |
| 98 | **apron** (trochee) / **pastry** (trochee) | assonance | same scene: bakery kitchen | Flour on my apron, pastry in the oven |
| 99 | **bacon** (trochee) / **gravy** (trochee) | assonance | same scene: hearty breakfast | Bacon sizzling, gravy on the side |
| 100 | **crayon** (trochee) / **painting** (trochee) | assonance | same domain: kids art supplies | A crayon sketch became a painting on the wall |

**Near-misses rejected (Long A)**

1. **upgrade / degrade** — A perfect rhyme and clean antonym pair, but both words are built on the same root "grade", so the rhyme is repetition rather than a true rhyme.
2. **maintain / sustain** — Tight synonyms and a perfect rhyme, but both share the bound root "-tain" (Latin tenere), so the rhyming syllable is the same morpheme.
3. **daylight / twilight** — A lovely day-versus-dusk contrast, but the slant link comes entirely from the shared morpheme "light".
4. **grateful / graceful** — Warm, positive words, but both end in an l-controlled "-ful" syllable, and the shared sound sits largely in that suffix.
5. **away / astray** — A perfect iamb rhyme with related meaning, but astray carries a negative sense of being lost or going wrong.

## Long E

/iː/ as in *peaceful, dreamy* — CMU `IY` under primary stress.

| # | Pair | Rhyme type | Relationship | One-line example use |
|---|---|---|---|---|
| 1 | **easy** (trochee) / **breezy** (trochee) | perfect | synonyms: carefree and light | Keep it easy, keep it breezy, let the summer carry you |
| 2 | **gleaming** (trochee) / **beaming** (trochee) | perfect | synonyms: shining with light | Your gleaming eyes and beaming smile light up the room |
| 3 | **indeed** (iamb) / **agreed** (iamb) | perfect | synonyms: yes, of course | Indeed, my love, we both agreed to dance tonight |
| 4 | **supreme** (iamb) / **extreme** (iamb) | perfect | synonyms: utmost highest degree | A love supreme, a joy extreme, we're soaring high |
| 5 | **teaching** (trochee) / **preaching** (trochee) | perfect | synonyms: sharing a lesson | She's teaching love, not preaching rules, just living kind |
| 6 | **neatly** (trochee) / **sweetly** (trochee) | perfect | synonyms: done with gentle care | You fold my letters neatly and you sign them sweetly |
| 7 | **easing** (trochee) / **pleasing** (trochee) | perfect | synonyms: soft and soothing | A gentle breeze so easing and so pleasing on my skin |
| 8 | **believe** (iamb) / **achieve** (iamb) | perfect | cause/effect: faith fuels success | If you believe, then you'll achieve the stars you chase |
| 9 | **reading** (trochee) / **leading** (trochee) | perfect | cause/effect: readers become leaders | Keep on reading and you'll soon be leading the way |
| 10 | **relief** (iamb) / **belief** (iamb) | perfect | cause/effect: faith brings comfort | Sweet relief arrived with my belief that dawn would come |
| 11 | **relieved** (iamb) / **achieved** (iamb) | perfect | cause/effect: goal brings ease | We're so relieved, the dream's achieved at last |
| 12 | **receive** (iamb) / **believe** (iamb) | perfect | cause/effect: trust then gain | Open up your heart, believe, and you'll receive |
| 13 | **teaching** (trochee) / **reaching** (trochee) | perfect | cause/effect: lessons touch hearts | Teaching kindness, reaching every heart in town |
| 14 | **proceed** (iamb) / **agreed** (iamb) | perfect | cause/effect: consent then action | Once we agreed, we could proceed with open hearts |
| 15 | **meeting** (trochee) / **greeting** (trochee) | perfect | same scene: friendly hello | Every meeting starts with a greeting full of sunshine |
| 16 | **creamy** (trochee) / **dreamy** (trochee) | perfect | same scene: sweet dessert night | Creamy vanilla on a dreamy summer night |
| 17 | **streaming** (trochee) / **gleaming** (trochee) | perfect | same scene: sunlight pouring in | Sunlight streaming, every window gleaming gold |
| 18 | **streaming** (trochee) / **beaming** (trochee) | perfect | same scene: sunny morning glow | Sunlight streaming through the curtains and you're beaming back at me |
| 19 | **fleeting** (trochee) / **meeting** (trochee) | perfect | same scene: brief encounter | A fleeting meeting on the train became forever |
| 20 | **seating** (trochee) / **eating** (trochee) | perfect | same scene: dinner table | Find your seating, start the eating, the feast is here |
| 21 | **beaches** (trochee) / **peaches** (trochee) | perfect | same scene: summer seaside | Sandy beaches, sunny peaches, summer in our hands |
| 22 | **elite** (iamb) / **compete** (iamb) | perfect | same domain: top-level contest | The elite compete beneath the stadium lights |
| 23 | **unique** (iamb) / **boutique** (iamb) | perfect | same domain: special little shop | A unique boutique on a cobblestone street |
| 24 | **treated** (trochee) / **greeted** (trochee) | perfect | same scene: welcomed guests | We were greeted with a hug and treated like family |
| 25 | **seated** (trochee) / **greeted** (trochee) | perfect | same scene: welcomed dinner guests | Every guest was greeted warmly and seated by the fire |
| 26 | **esteem** (iamb) / **supreme** (iamb) | perfect | same domain: highest regard | Hold yourself in high esteem, your heart supreme |
| 27 | **redeem** (iamb) / **esteem** (iamb) | perfect | same domain: restored self-worth | Let kindness redeem the day and lift your self-esteem |
| 28 | **season** (trochee) / **reason** (trochee) | perfect | same domain: purpose in time | For every season there's a reason to sing |
| 29 | **seeking** (trochee) / **speaking** (trochee) | perfect | same domain: honest truth telling | Seeking truth and speaking kindly every day |
| 30 | **serene** (iamb) / **ravine** (iamb) | perfect | same scene: quiet green valley | The river runs serene along the green ravine |
| 31 | **marine** (iamb) / **serene** (iamb) | perfect | same scene: calm blue sea | A marine blue bay, so calm and so serene |
| 32 | **feeding** (trochee) / **seeding** (trochee) | perfect | same scene: garden care | Seeding rows and feeding roots, the garden grows |
| 33 | **steamy** (trochee) / **creamy** (trochee) | perfect | same scene: morning latte | A steamy, creamy latte warms my morning hands |
| 34 | **cuisine** (iamb) / **caffeine** (iamb) | perfect | same scene: cozy corner cafe | French cuisine and fresh caffeine in a corner cafe |
| 35 | **canteen** (iamb) / **cuisine** (iamb) | perfect | same domain: dining hall food | The little canteen serves a homemade cuisine we love |
| 36 | **antique** (iamb) / **boutique** (iamb) | perfect | same scene: vintage shopping day | Antique lamps glow in a little boutique downtown |
| 37 | **teaches** (trochee) / **speeches** (trochee) | perfect | same domain: inspiring lessons | She teaches hope through speeches full of light |
| 38 | **keeping** (trochee) / **sleeping** (trochee) | perfect | same scene: tender night watch | I'll be keeping watch while you are sleeping |
| 39 | **retreat** (iamb) / **discreet** (iamb) | perfect | same scene: quiet hideaway | A discreet retreat beside the lake, just us two |
| 40 | **routine** (iamb) / **machine** (iamb) | perfect | same domain: steady daily rhythm | Our morning routine hums like a happy machine |
| 41 | **unseen** (iamb) / **between** (iamb) | perfect | same domain: hidden spaces | The love unseen that lives between the lines |
| 42 | **leaping** (trochee) / **sweeping** (trochee) | perfect | same scene: graceful dance motion | Leaping, sweeping, spinning round the ballroom floor |
| 43 | **complete** (iamb) / **repeat** (iamb) | perfect | same domain: favorite song loop | The song's complete, so press repeat and sing along |
| 44 | **reaches** (trochee) / **beaches** (trochee) | perfect | same scene: tide meets shore | The morning tide reaches golden beaches by the bay |
| 45 | **unique** (iamb) / **alike** (iamb) | slant | antonyms: different versus same | We're each unique, yet in our hearts alike |
| 46 | **leading** (trochee) / **heading** (trochee) | slant | synonyms: steering the team | She's heading up the choir and leading us in song |
| 47 | **proceed** (iamb) / **ahead** (iamb) | slant | synonyms: move forward onward | We proceed with courage, looking straight ahead |
| 48 | **serene** (iamb) / **benign** (iamb) | slant | synonyms: gentle and calm | Your smile is serene, your heart benign and kind |
| 49 | **elite** (iamb) / **unique** (iamb) | slant | synonyms: exceptional and rare | Elite and unique, you're one of a kind |
| 50 | **sleeping** (trochee) / **napping** (trochee) | slant | synonyms: resting tired eyes | The cat is napping while the baby's sleeping |
| 51 | **complete** (iamb) / **ignite** (iamb) | slant | antonyms: start versus finish | We ignite the spark and dance until it's complete |
| 52 | **between** (iamb) / **within** (iamb) | slant | synonyms: inside the space | Between the stars and deep within my heart |
| 53 | **cleaning** (trochee) / **gleaming** (trochee) | slant | cause/effect: scrubbing makes shine | Cleaning every window till the glass is gleaming |
| 54 | **compete** (iamb) / **succeed** (iamb) | slant | cause/effect: effort brings victory | We compete with heart and that is how we succeed |
| 55 | **complete** (iamb) / **delight** (iamb) | slant | cause/effect: finishing brings joy | The puzzle's complete, oh what a sweet delight |
| 56 | **succeed** (iamb) / **decide** (iamb) | slant | cause/effect: choice then success | Decide to dream and you'll succeed someday |
| 57 | **reading** (trochee) / **freedom** (trochee) | slant | cause/effect: books bring liberty | Every page of reading gives my spirit freedom |
| 58 | **sweetly** (trochee) / **deeply** (trochee) | slant | same domain: tender loving ways | Love me sweetly, love me deeply, all night long |
| 59 | **meaning** (trochee) / **dreaming** (trochee) | slant | same domain: purpose and hope | Finding meaning in the dreaming of the night |
| 60 | **meeting** (trochee) / **speaking** (trochee) | slant | same scene: friendly conversation | At every meeting you were speaking words of hope |
| 61 | **easy** (trochee) / **cozy** (trochee) | slant | same domain: relaxed comfort | Easy mornings in a cozy little room |
| 62 | **breezy** (trochee) / **lazy** (trochee) | slant | same scene: summer afternoon | A breezy, lazy Sunday by the shore |
| 63 | **season** (trochee) / **frozen** (trochee) | slant | same scene: winter lake | The skating season on the frozen lake |
| 64 | **season** (trochee) / **easing** (trochee) | slant | same scene: winter softening | The cold is easing as the season turns to spring |
| 65 | **believe** (iamb) / **alive** (iamb) | slant | same domain: hopeful vitality | When I believe, I feel alive again |
| 66 | **beaming** (trochee) / **blooming** (trochee) | slant | same domain: radiant joy | You're beaming like the roses blooming in the sun |
| 67 | **greeting** (trochee) / **speaking** (trochee) | slant | same scene: warm welcome words | A friendly greeting, softly speaking welcome home |
| 68 | **eating** (trochee) / **feeding** (trochee) | slant | same domain: family mealtime | We're eating lunch and feeding ducks beside the pond |
| 69 | **neatly** (trochee) / **tightly** (trochee) | slant | same domain: tidy careful packing | Pack it neatly, wrap it tightly, send it home |
| 70 | **seeking** (trochee) / **beacon** (trochee) | slant | same scene: searching ship's light | Seeking home, I find a beacon on the shore |
| 71 | **even** (trochee) / **breathing** (trochee) | slant | same scene: calm restful sleep | Your breathing slow and even as you sleep |
| 72 | **sweetie** (trochee) / **sleepy** (trochee) | slant | same scene: bedtime cuddle | Goodnight my sleepy sweetie, close your eyes |
| 73 | **compete** (iamb) / **debate** (iamb) | slant | same domain: friendly contest | We debate and compete, but we're friends at the end |
| 74 | **receive** (iamb) / **arrive** (iamb) | slant | same scene: gift delivery day | The letters arrive and I receive your love |
| 75 | **leaving** (trochee) / **moving** (trochee) | slant | same domain: relocating home | We're leaving town and moving to the sea |
| 76 | **marine** (iamb) / **lagoon** (iamb) | slant | same scene: tropical blue water | Marine blue waves in a quiet lagoon |
| 77 | **increase** (iamb) / **deepen** (trochee) | assonance | synonyms: growing stronger | Let our love increase and deepen with the years |
| 78 | **succeed** (iamb) / **achieve** (iamb) | assonance | synonyms: reaching success | Together we'll succeed and we'll achieve it all |
| 79 | **release** (iamb) / **freedom** (trochee) | assonance | synonyms: liberation and escape | Release the doves and let them fly to freedom |
| 80 | **relief** (iamb) / **easing** (trochee) | assonance | synonyms: soothing comfort | What a sweet relief to feel the busy day easing into night |
| 81 | **sleeping** (trochee) / **dreaming** (trochee) | assonance | cause/effect: rest brings dreams | Sleeping under starlight, dreaming of the sea |
| 82 | **treaty** (trochee) / **agreed** (iamb) | assonance | cause/effect: peace pact signed | The treaty's signed and every heart agreed |
| 83 | **discreet** (iamb) / **secret** (trochee) | assonance | same domain: keeping confidences | Be discreet and keep my secret close to your heart |
| 84 | **secret** (trochee) / **keeping** (trochee) | assonance | same domain: trusted confidence | Keeping every secret that you whisper to me |
| 85 | **release** (iamb) / **freely** (trochee) | assonance | same domain: letting go | Release the kite and let it fly so freely |
| 86 | **teaching** (trochee) / **reading** (trochee) | assonance | same domain: classroom learning | Teaching little ones the joy of reading |
| 87 | **seeking** (trochee) / **reaching** (trochee) | assonance | same domain: striving for more | Always seeking, always reaching for the stars |
| 88 | **deeply** (trochee) / **breathing** (trochee) | assonance | same scene: calm restful air | Breathing deeply in the cool pine air |
| 89 | **breathing** (trochee) / **easy** (trochee) | assonance | same domain: relaxed calm | Breathing easy by the open window |
| 90 | **cleaning** (trochee) / **sweeping** (trochee) | assonance | same scene: household chores | Cleaning windows, sweeping floors, the house is shining |
| 91 | **sleepy** (trochee) / **dreamy** (trochee) | assonance | same scene: drowsy bedtime | A sleepy, dreamy lullaby to end the day |
| 92 | **evening** (trochee) / **dreamy** (trochee) | assonance | same scene: soft twilight | A dreamy evening glowing pink and gold |
| 93 | **weekend** (trochee) / **freedom** (trochee) | assonance | same domain: time off | The weekend comes and brings a taste of freedom |
| 94 | **seaside** (trochee) / **beaches** (trochee) | assonance | part/whole: beaches of seaside | A seaside town with sandy beaches all around |
| 95 | **leafy** (trochee) / **breezy** (trochee) | assonance | same scene: summer park | A leafy lane on a breezy afternoon |
| 96 | **evening** (trochee) / **sleepy** (trochee) | assonance | same scene: quiet nightfall | The evening settles, sleepy and so still |
| 97 | **kiwi** (trochee) / **peaches** (trochee) | assonance | same domain: fresh fruit basket | Kiwi, peaches, berries in a picnic basket |
| 98 | **cheesy** (trochee) / **pizza** (trochee) | assonance | same domain: comfort food | A cheesy pizza shared with friends on Friday night |
| 99 | **zebra** (trochee) / **cheetah** (trochee) | assonance | same scene: savanna safari | A zebra and a cheetah on the golden plain |
| 100 | **greenhouse** (trochee) / **seedlings** (trochee) | assonance | same scene: spring garden | In the greenhouse, seedlings reach toward the sun |

**Near-misses rejected (Long E)**

1. **sixteen / eighteen** — A perfect rhyme, but both words share the -teen morpheme, so it is repetition rather than rhyme.
2. **seeing / viewing** — The slant comes only from the -ing suffix, because the stems see and view share no sounds.
3. **peaceful / easy** — Peaceful ends in an l-controlled -ful syllable, so it fails the no-l-control rule and has no sound link to easy.
4. **weeping / sleeping** — A perfect rhyme in a bedtime scene, but weeping is a grief word, which breaks the positive-words rule.
5. **agree / degree** — A perfect rhyme, but the meaning link is too loose, since a degree has nothing to do with agreeing.

## Long I

/aɪ/ as in *delight, shining* — CMU `AY` under primary stress.

| # | Pair | Rhyme type | Relationship | One-line example use |
|---|---|---|---|---|
| 1 | **brighten** (trochee) / **lighten** (trochee) | perfect | synonyms: fill with light | Let the morning brighten and the heavy clouds lighten |
| 2 | **sliding** (trochee) / **gliding** (trochee) | perfect | synonyms: smooth easy motion | We go sliding down the hill and gliding into spring |
| 3 | **spicy** (trochee) / **icy** (trochee) | perfect | antonyms: hot versus cold | Your spicy laugh could melt this icy winter night |
| 4 | **slightly** (trochee) / **lightly** (trochee) | perfect | synonyms: soft gentle touch | Lean in slightly and kiss me lightly on the cheek |
| 5 | **delight** (iamb) / **excite** (iamb) | perfect | synonyms: thrill and joy | You fill my days with delight and every hello will excite |
| 6 | **ignite** (iamb) / **alight** (iamb) | perfect | synonyms: set aflame | One small spark can ignite a heart and set the sky alight |
| 7 | **comply** (iamb) / **defy** (iamb) | perfect | antonyms: obey versus resist | Let the cautious comply, we will defy the gray with color |
| 8 | **reside** (iamb) / **abide** (iamb) | perfect | synonyms: dwell and stay | Where your kindness may reside, my heart will gladly abide |
| 9 | **provide** (iamb) / **supplied** (iamb) | perfect | synonyms: give what's needed | All the love you provide kept my hopeful heart supplied |
| 10 | **align** (iamb) / **combine** (iamb) | perfect | synonyms: bring together | When the stars align our voices combine in song |
| 11 | **thriving** (trochee) / **striving** (trochee) | perfect | cause/effect: effort brings flourishing | We kept striving through the seasons and now the garden's thriving |
| 12 | **alive** (iamb) / **revive** (iamb) | perfect | cause/effect: revival restores life | Your laughter can revive me and make me feel alive |
| 13 | **polite** (iamb) / **upright** (iamb) | perfect | synonyms: proper good conduct | Stay polite, stand upright, and let your kindness show |
| 14 | **brightness** (trochee) / **whiteness** (trochee) | perfect | synonyms: pale radiant glow | The brightness of the snow and the whiteness of the moon |
| 15 | **hiking** (trochee) / **biking** (trochee) | perfect | same domain: trail adventures | Summer days of hiking trails and biking down to the bay |
| 16 | **design** (iamb) / **refine** (iamb) | perfect | cause/effect: draft then polish | We sketch a bold design and refine it line by line |
| 17 | **shining** (trochee) / **lining** (trochee) | perfect | same scene: silver lining glow | There's a silver lining shining through the rain |
| 18 | **tiny** (trochee) / **shiny** (trochee) | perfect | same scene: small bright gem | A tiny shiny seashell glowing in your hand |
| 19 | **brightly** (trochee) / **nightly** (trochee) | perfect | same scene: stars each night | The stars shine brightly, nightly, just for you |
| 20 | **tonight** (iamb) / **delight** (iamb) | perfect | same scene: joyful evening | Dance with me tonight and lose yourself in pure delight |
| 21 | **invite** (iamb) / **tonight** (iamb) | perfect | same scene: evening gathering | I send this warm invite: come sing with us tonight |
| 22 | **polite** (iamb) / **invite** (iamb) | perfect | same domain: gracious manners | With a polite little bow I offer my invite |
| 23 | **ignite** (iamb) / **delight** (iamb) | perfect | cause/effect: spark kindles joy | One little song can ignite a night of pure delight |
| 24 | **slices** (trochee) / **spices** (trochee) | perfect | same scene: kitchen baking | Warm bread slices dusted with cinnamon and spices |
| 25 | **concise** (iamb) / **suffice** (iamb) | perfect | cause/effect: brevity is enough | A concise little kiss will suffice to say I love you |
| 26 | **brightly** (trochee) / **lightly** (trochee) | perfect | same domain: gentle radiance | Step lightly, smile brightly, the day belongs to you |
| 27 | **reply** (iamb) / **goodbye** (iamb) | perfect | same scene: farewell exchange | Wave goodbye and I will reply with a song |
| 28 | **arrived** (iamb) / **revived** (iamb) | perfect | cause/effect: spring restores fields | The moment spring arrived the sleepy fields revived |
| 29 | **riding** (trochee) / **gliding** (trochee) | perfect | same scene: smooth downhill ride | Riding on a sled and gliding down the snowy hill |
| 30 | **winding** (trochee) / **finding** (trochee) | perfect | same scene: wandering trail | Down the winding road we keep on finding home |
| 31 | **advice** (iamb) / **precise** (iamb) | perfect | same domain: clear counsel | Your advice is gentle, kind, and precise |
| 32 | **design** (iamb) / **align** (iamb) | perfect | same domain: careful layout | We plan a clean design and let every color align |
| 33 | **divine** (iamb) / **sublime** (iamb) | slant | synonyms: heavenly glorious | Your voice is divine and the melody sublime |
| 34 | **sublime** (iamb) / **supreme** (iamb) | slant | synonyms: highest excellence | A sunset so sublime, a joy supreme |
| 35 | **guiding** (trochee) / **leading** (trochee) | slant | synonyms: show the way | Your love is guiding me and leading me home |
| 36 | **hiking** (trochee) / **trekking** (trochee) | slant | synonyms: long journeys on foot | We went hiking through the hills and trekking by the stream |
| 37 | **divine** (iamb) / **serene** (iamb) | slant | synonyms: heavenly calm | In this divine and serene morning light |
| 38 | **polite** (iamb) / **discreet** (iamb) | slant | synonyms: tactful and courteous | Polite and discreet, she kept our secret sweet |
| 39 | **thriving** (trochee) / **living** (trochee) | slant | synonyms: full flourishing life | We are living freely and our hearts are thriving |
| 40 | **writing** (trochee) / **typing** (trochee) | slant | synonyms: putting words down | I'm typing out these verses, writing all night long |
| 41 | **shining** (trochee) / **raining** (trochee) | slant | antonyms: sun versus rain | Whether it is raining or the sun is shining, I'm with you |
| 42 | **brightest** (trochee) / **greatest** (trochee) | slant | synonyms: very best | You are the brightest light and the greatest gift I know |
| 43 | **devised** (iamb) / **composed** (iamb) | slant | synonyms: crafted and created | She devised a melody and composed it just for you |
| 44 | **lighting** (trochee) / **guiding** (trochee) | slant | cause/effect: light shows the way | The lantern lighting up the path is guiding us home |
| 45 | **wisely** (trochee) / **nicely** (trochee) | slant | same domain: good conduct | Speak wisely, treat others nicely, and the world will smile |
| 46 | **silent** (trochee) / **island** (trochee) | slant | same scene: quiet isle | On a silent island where the soft waves sing |
| 47 | **brightness** (trochee) / **sweetness** (trochee) | slant | same domain: pleasant qualities | The brightness of your smile, the sweetness of your song |
| 48 | **brightly** (trochee) / **sweetly** (trochee) | slant | same domain: pleasant manner | Birds sing sweetly as the sun shines brightly |
| 49 | **timeless** (trochee) / **seamless** (trochee) | slant | same domain: flawless enduring grace | A timeless dance, a seamless glide across the floor |
| 50 | **climbing** (trochee) / **blooming** (trochee) | slant | same scene: garden roses | Climbing roses blooming on the garden gate |
| 51 | **rising** (trochee) / **praising** (trochee) | slant | same scene: morning hymn | With the sun rising high we are praising the day |
| 52 | **divine** (iamb) / **amen** (iamb) | slant | same domain: prayerful worship | The chorus sounded so divine that we all sang amen |
| 53 | **ignite** (iamb) / **create** (iamb) | slant | cause/effect: spark makes art | Ignite your spark and create something new |
| 54 | **arrive** (iamb) / **achieve** (iamb) | slant | cause/effect: reaching the goal | When we arrive we'll see the dreams that we achieve |
| 55 | **driving** (trochee) / **moving** (trochee) | slant | same domain: travel in motion | Driving down the coast with music moving through our souls |
| 56 | **shiny** (trochee) / **penny** (trochee) | slant | same scene: lucky coin | A shiny penny tossed into a wishing fountain |
| 57 | **decide** (iamb) / **agreed** (iamb) | slant | cause/effect: choice brings agreement | We sat down to decide and we happily agreed |
| 58 | **quiet** (trochee) / **silent** (trochee) | assonance | synonyms: hushed and still | A quiet field, a silent snow, a peaceful night |
| 59 | **tiny** (trochee) / **giant** (trochee) | assonance | antonyms: small versus huge | From tiny seeds a giant oak will grow |
| 60 | **tiny** (trochee) / **mighty** (trochee) | assonance | antonyms: small versus strong | A tiny seed can grow into a mighty tree |
| 61 | **hiding** (trochee) / **finding** (trochee) | assonance | antonyms: hidden versus found | You were hiding in the garden and I keep finding you there |
| 62 | **giant** (trochee) / **mighty** (trochee) | assonance | synonyms: huge and strong | A giant wave, a mighty ocean song |
| 63 | **benign** (iamb) / **kindness** (trochee) | assonance | synonyms: gentle goodwill | A benign old heart that's full of kindness |
| 64 | **kindly** (trochee) / **nicely** (trochee) | assonance | synonyms: gentle good manners | Ask her kindly and she'll answer nicely |
| 65 | **tidy** (trochee) / **precise** (iamb) | assonance | synonyms: neat and exact | A tidy little garden laid out neat and precise |
| 66 | **highest** (trochee) / **finest** (trochee) | assonance | synonyms: top quality | The highest praise for the finest friend I know |
| 67 | **supply** (iamb) / **provide** (iamb) | assonance | synonyms: furnish and give | The rains supply the river and the river will provide |
| 68 | **guidance** (trochee) / **advice** (iamb) | assonance | synonyms: wise counsel given | Thank you for your gentle guidance and your kind advice |
| 69 | **benign** (iamb) / **kindly** (trochee) | assonance | synonyms: gentle and kind | A benign old sun that shines so kindly on the town |
| 70 | **sublime** (iamb) / **timeless** (trochee) | assonance | synonyms: eternal and grand | A timeless song, a love sublime |
| 71 | **timeless** (trochee) / **priceless** (trochee) | assonance | synonyms: precious beyond measure | These timeless moments are priceless to me |
| 72 | **lively** (trochee) / **vibrant** (trochee) | assonance | synonyms: full of energy | A lively crowd along a vibrant summer street |
| 73 | **excite** (iamb) / **lively** (trochee) | assonance | synonyms: full of spark | A lively tune will always excite the crowd |
| 74 | **climbing** (trochee) / **rising** (trochee) | assonance | synonyms: going upward | Climbing higher, rising with the morning sun |
| 75 | **biking** (trochee) / **riding** (trochee) | assonance | synonyms: pedaling along | Biking through the city, riding by the bay |
| 76 | **flying** (trochee) / **gliding** (trochee) | assonance | synonyms: airborne motion | Flying over valleys, gliding on the breeze |
| 77 | **alive** (iamb) / **thriving** (trochee) | assonance | synonyms: full of life | So alive and thriving in the summer sun |
| 78 | **advice** (iamb) / **wisely** (trochee) | assonance | cause/effect: counsel guides choices | Take my advice and spend your summers wisely |
| 79 | **wisely** (trochee) / **kindly** (trochee) | assonance | same domain: virtuous ways | Choose wisely, speak kindly, love freely |
| 80 | **finest** (trochee) / **brightest** (trochee) | assonance | synonyms: the very best | The finest friend and the brightest soul I know |
| 81 | **rising** (trochee) / **shining** (trochee) | assonance | same scene: sunrise glow | The sun is rising, shining on the bay |
| 82 | **tonight** (iamb) / **twilight** (trochee) | assonance | same scene: evening sky | In the soft twilight we will hold hands tonight |
| 83 | **arrive** (iamb) / **driving** (trochee) | assonance | cause/effect: drive then arrive | Keep on driving and soon we will arrive |
| 84 | **hiking** (trochee) / **climbing** (trochee) | assonance | same domain: mountain trail | Hiking up the ridge and climbing toward the clouds |
| 85 | **flying** (trochee) / **pilot** (trochee) | assonance | same domain: aviation | The pilot sings while flying through the dawn |
| 86 | **shiny** (trochee) / **diamond** (trochee) | assonance | same scene: jewel sparkle | A shiny diamond glinting in the candlelight |
| 87 | **invite** (iamb) / **dining** (trochee) | assonance | same scene: dinner party | Accept my invite to dining by candlelight |
| 88 | **spicy** (trochee) / **dining** (trochee) | assonance | same scene: dinner table | Spicy soup and laughter while we're dining with friends |
| 89 | **diamond** (trochee) / **priceless** (trochee) | assonance | same domain: precious jewels | A diamond in the snow, a priceless winter glow |
| 90 | **quiet** (trochee) / **private** (trochee) | assonance | synonyms: secluded and calm | A quiet, private corner just for two |
| 91 | **icy** (trochee) / **whiteness** (trochee) | assonance | same scene: winter snow | Icy branches sparkle in the whiteness of the dawn |
| 92 | **island** (trochee) / **lighthouse** (trochee) | assonance | same scene: coastal night | An island lighthouse glowing in the bay |
| 93 | **guiding** (trochee) / **lighthouse** (trochee) | assonance | cause/effect: beacon guides ships | The lighthouse keeps on guiding sailors home |
| 94 | **highway** (trochee) / **driving** (trochee) | assonance | same scene: road trip | Driving down the highway with the windows open wide |
| 95 | **skyline** (trochee) / **highway** (trochee) | assonance | same scene: city drive | The skyline glitters as we cruise the open highway |
| 96 | **icing** (trochee) / **slices** (trochee) | assonance | same scene: birthday cake | Birthday cake with sugar icing cut in happy slices |
| 97 | **silence** (trochee) / **twilight** (trochee) | assonance | same scene: evening hush | In the gentle silence of the purple twilight |
| 98 | **ivy** (trochee) / **lilac** (trochee) | assonance | same scene: cottage garden | Ivy on the fence and lilac by the gate |
| 99 | **rhino** (trochee) / **bison** (trochee) | assonance | same domain: mighty grazing beasts | The rhino and the bison roam the open plain |
| 100 | **lion** (trochee) / **rhino** (trochee) | assonance | same domain: safari wildlife | A lion and a rhino resting in the sun |

**Near-misses rejected (Long I)**

1. **precise / concise** — Both are prefix swaps on the same Latin root -cise ("cut"), so the perfect rhyme is repetition rather than rhyme.
2. **island / highland** — Island comes from Old English ieg-land, so the two words share the land morpheme despite the perfect rhyme and landscape link.
3. **flying / glowing** — The validator calls it slant, but the only shared sounds come from the -ing suffix because the stems fly and glow share nothing.
4. **quiet / riot** — Perfect rhyme with a vivid contrast, but riot is a violence word and breaks the positive-words rule.
5. **hiking / walking** — Tight synonyms with a slant rhyme, but the silent L in walk counts as l-controlled, so walking does not qualify.

## Long O

/oʊ/ as in *glowing, hopeful* — CMU `OW` under primary stress.

| # | Pair | Rhyme type | Relationship | One-line example use |
|---|---|---|---|---|
| 1 | **roasted** (trochee) / **toasted** (trochee) | perfect | synonyms: browned by fire | We roasted chestnuts and we toasted bread beside the fire |
| 2 | **cozy** (trochee) / **rosy** (trochee) | perfect | synonyms: warm and snug | Your cheeks turn rosy in this cozy little room |
| 3 | **focus** (trochee) / **locus** (trochee) | perfect | synonyms: center of attention | You're the focus of my heart, the locus of my light |
| 4 | **going** (trochee) / **flowing** (trochee) | perfect | synonyms: moving steadily onward | Keep the music flowing and the good times going |
| 5 | **disclose** (iamb) / **expose** (iamb) | perfect | synonyms: reveal hidden feelings | I'll disclose my secret heart and expose the love inside |
| 6 | **noted** (trochee) / **quoted** (trochee) | perfect | synonyms: remarked and cited | She noted every kind word and we quoted her all summer |
| 7 | **slowing** (trochee) / **going** (trochee) | perfect | antonyms: slowing versus going | Never slowing, always going, we chase the morning sun |
| 8 | **sowing** (trochee) / **growing** (trochee) | perfect | cause/effect: seeds become sprouts | We are sowing seeds of kindness, watch them growing every day |
| 9 | **notion** (trochee) / **motion** (trochee) | perfect | cause/effect: idea sparks action | One bright notion set the whole wide world in motion |
| 10 | **floating** (trochee) / **boating** (trochee) | perfect | same scene: lazy lake day | Summer days of boating, lazy hours of floating free |
| 11 | **ocean** (trochee) / **motion** (trochee) | perfect | same scene: rolling sea waves | The ocean keeps its gentle motion, rocking us to sleep |
| 12 | **roses** (trochee) / **noses** (trochee) | perfect | same scene: smelling garden flowers | We pressed our noses into roses blooming by the gate |
| 13 | **glowing** (trochee) / **snowing** (trochee) | perfect | same scene: fireside winter night | Outside it's snowing, inside the fire is glowing |
| 14 | **snowing** (trochee) / **blowing** (trochee) | perfect | same scene: gentle winter flurry | It's softly snowing and the winter wind is blowing |
| 15 | **bowing** (trochee) / **showing** (trochee) | perfect | same scene: stage curtain call | After the showing, all the dancers keep on bowing |
| 16 | **flowing** (trochee) / **rowing** (trochee) | perfect | same scene: river boat ride | We go rowing down the river with the waters flowing slow |
| 17 | **spoken** (trochee) / **token** (trochee) | perfect | same scene: vows and rings | With every promise spoken, this ring's my token true |
| 18 | **arose** (iamb) / **propose** (iamb) | perfect | same scene: sunrise marriage proposal | As the golden sun arose, I knelt down to propose |
| 19 | **hosted** (trochee) / **toasted** (trochee) | perfect | same scene: dinner party cheers | We hosted all our friends and toasted to the year |
| 20 | **hosting** (trochee) / **roasting** (trochee) | perfect | same scene: holiday dinner feast | We are hosting the whole family, roasting turkey through the night |
| 21 | **ocean** (trochee) / **lotion** (trochee) | perfect | same scene: sunny beach day | Sparkling ocean, coconut lotion, summer on our skin |
| 22 | **plateau** (iamb) / **below** (iamb) | perfect | same scene: mountain valley view | From the high plateau the valley sparkles far below |
| 23 | **chateau** (iamb) / **plateau** (iamb) | perfect | same scene: hilltop French estate | A stone chateau stands proud upon the green plateau |
| 24 | **baroque** (iamb) / **bespoke** (iamb) | perfect | same domain: ornate fine craftsmanship | A baroque frame, a bespoke gown, a night of golden grace |
| 25 | **remote** (iamb) / **afloat** (iamb) | perfect | same scene: drifting distant boat | On a remote blue sea we drift afloat and free |
| 26 | **holy** (trochee) / **lowly** (trochee) | perfect | same scene: humble manger hymn | A holy light fell softly on that lowly stable bed |
| 27 | **holy** (trochee) / **slowly** (trochee) | perfect | same scene: reverent church bells | Slowly the holy bells ring out across the sleepy town |
| 28 | **hello** (iamb) / **ago** (iamb) | perfect | same scene: old friend reunion | Hello, my friend, from all those happy years ago |
| 29 | **glowing** (trochee) / **growing** (trochee) | perfect | same scene: thriving sunlit garden | The garden's glowing and the seedlings keep on growing |
| 30 | **abode** (iamb) / **unload** (iamb) | perfect | same scene: moving-in day | We unload the boxes at our sweet new abode |
| 31 | **joking** (trochee) / **poking** (trochee) | perfect | same scene: playful friendly teasing | Joking with my brothers, poking fun all afternoon |
| 32 | **proton** (trochee) / **photon** (trochee) | perfect | same domain: atomic particle physics | Every proton, every photon, hums the song of light |
| 33 | **notice** (trochee) / **focus** (trochee) | slant | synonyms: paying close attention | Notice every moment, focus on the light |
| 34 | **bespoke** (iamb) / **unique** (iamb) | slant | synonyms: one of a kind | A bespoke love, unique as morning light |
| 35 | **devote** (iamb) / **commit** (iamb) | slant | synonyms: pledge full dedication | I devote my life to you, commit my every day |
| 36 | **compose** (iamb) / **devise** (iamb) | slant | synonyms: create and craft | I'll compose a melody and devise a little rhyme |
| 37 | **coaching** (trochee) / **teaching** (trochee) | slant | synonyms: guiding young learners | Coaching little leaguers, teaching them to dream |
| 38 | **quoting** (trochee) / **citing** (trochee) | slant | synonyms: referencing others' words | Quoting poets, citing stars, I tell you how I feel |
| 39 | **noting** (trochee) / **writing** (trochee) | slant | synonyms: jotting words down | Noting every sunset, writing every dream |
| 40 | **noted** (trochee) / **stated** (trochee) | slant | synonyms: remarked and declared | I noted what you stated: love is all we need |
| 41 | **sewing** (trochee) / **showing** (trochee) | perfect | same scene: fashion design runway | Months of sewing led to showing gowns upon the stage |
| 42 | **throwing** (trochee) / **sowing** (trochee) | perfect | cause/effect: scattered seeds planted | Throwing seeds across the field, we're sowing hope for spring |
| 43 | **lotus** (trochee) / **focus** (trochee) | slant | same domain: calm meditation practice | Sit still like a lotus, breathe and find your focus |
| 44 | **remote** (iamb) / **retreat** (iamb) | slant | same scene: secluded mountain getaway | A remote retreat where the river meets the sky |
| 45 | **baroque** (iamb) / **antique** (iamb) | slant | same domain: ornate vintage art | Baroque mirrors and antique lace adorn the hall |
| 46 | **bespoke** (iamb) / **boutique** (iamb) | slant | same domain: tailored fashion shop | From the boutique, a bespoke dress of silk |
| 47 | **abode** (iamb) / **reside** (iamb) | slant | same domain: dwelling at home | In this humble abode is where our hearts reside |
| 48 | **cozy** (trochee) / **lazy** (trochee) | slant | same scene: slow restful Sunday | A cozy blanket on a lazy Sunday morning |
| 49 | **rosy** (trochee) / **daisy** (trochee) | slant | same scene: blooming spring garden | Rosy cheeks and a daisy tucked behind your ear |
| 50 | **roses** (trochee) / **vases** (trochee) | slant | same scene: flowers on display | Fill the crystal vases with the roses from the yard |
| 51 | **poses** (trochee) / **muses** (trochee) | slant | same scene: artist's studio session | The painter muses while the model poses in the light |
| 52 | **posing** (trochee) / **gazing** (trochee) | slant | same scene: portrait photo shoot | She's posing by the window, gazing at the sea |
| 53 | **roasted** (trochee) / **tasted** (trochee) | slant | cause/effect: cooked then savored | We roasted corn and tasted summer on the porch |
| 54 | **soaking** (trochee) / **floating** (trochee) | slant | same scene: lazy pool day | Soaking up the sunshine, floating on the pool |
| 55 | **poet** (trochee) / **quiet** (trochee) | slant | same scene: contemplative writing hour | The poet loves the quiet hours before the dawn |
| 56 | **invoke** (iamb) / **devote** (iamb) | slant | same domain: prayerful heartfelt dedication | I invoke the stars and devote my heart to you |
| 57 | **roaming** (trochee) / **dreaming** (trochee) | slant | same scene: wandering daydream afternoon | Roaming through the meadows, dreaming of the sea |
| 58 | **slogan** (trochee) / **spoken** (trochee) | slant | same domain: catchy spoken phrase | A hopeful slogan spoken softly can change the world |
| 59 | **solo** (trochee) / **halo** (trochee) | slant | same scene: angelic choir spotlight | She sings her solo with a golden halo glow |
| 60 | **open** (trochee) / **hoping** (trochee) | slant | same feeling: open hopeful heart | Keep your heart wide open, keep on hoping for the dawn |
| 61 | **poem** (trochee) / **flowing** (trochee) | slant | same domain: lyrical flowing verse | Let the poem keep on flowing like a river to the sea |
| 62 | **woven** (trochee) / **clothing** (trochee) | slant | same domain: textile handmade garments | Woven threads of gold become the clothing that you wear |
| 63 | **cologne** (iamb) / **champagne** (iamb) | slant | same scene: elegant evening out | A splash of cologne, a glass of champagne tonight |
| 64 | **alone** (iamb) / **serene** (iamb) | slant | same feeling: peaceful quiet solitude | Alone beside the lake, serene as the dawn |
| 65 | **rosy** (trochee) / **hazy** (trochee) | slant | same scene: soft summer dusk | A rosy sky above a hazy summer field |
| 66 | **compose** (iamb) / **revise** (iamb) | slant | same domain: songwriting draft work | I compose a verse at midnight and revise it in the dawn |
| 67 | **alone** (iamb) / **solo** (trochee) | assonance | synonyms: on one's own | I'm not alone, though I'm singing solo tonight |
| 68 | **only** (trochee) / **solo** (trochee) | assonance | synonyms: single and alone | The only voice tonight, a solo sweet and clear |
| 69 | **open** (trochee) / **closing** (trochee) | assonance | antonyms: open versus closing | One door is closing, another swinging open |
| 70 | **composed** (iamb) / **stoic** (trochee) | assonance | synonyms: calm and unshaken | Composed and stoic, steady as the mountain |
| 71 | **opus** (trochee) / **poem** (trochee) | assonance | synonyms: creative written work | This poem is my opus, every word for you |
| 72 | **soda** (trochee) / **cola** (trochee) | assonance | synonyms: fizzy soft drink | Cherry cola, orange soda, summer on the porch |
| 73 | **roaming** (trochee) / **nomad** (trochee) | assonance | synonyms: wandering traveler life | A nomad roaming free beneath the desert stars |
| 74 | **abode** (iamb) / **homestead** (trochee) | assonance | synonyms: dwelling place home | Our homestead is a humble, happy abode |
| 75 | **rotate** (trochee) / **motion** (trochee) | assonance | synonyms: turning spinning movement | Watch the planets rotate in their graceful motion |
| 76 | **compose** (iamb) / **poem** (trochee) | assonance | cause/effect: writing creates verse | I'll compose a poem for you by candlelight |
| 77 | **clothing** (trochee) / **sewing** (trochee) | assonance | cause/effect: stitching makes garments | Grandma's sewing turned to clothing for us all |
| 78 | **coaching** (trochee) / **trophy** (trochee) | assonance | cause/effect: training earns prize | Years of coaching brought the shiny trophy home |
| 79 | **bestowed** (iamb) / **trophy** (trochee) | assonance | cause/effect: award granted honor | The trophy bestowed upon the team that never quit |
| 80 | **promote** (iamb) / **bonus** (trochee) | assonance | cause/effect: promotion brings reward | They'll promote you soon, and there's a bonus on the way |
| 81 | **produce** (trochee) / **growing** (trochee) | assonance | cause/effect: farming yields harvest | Our garden keeps on growing, fresh produce every summer day |
| 82 | **romance** (trochee) / **propose** (iamb) | assonance | cause/effect: love leads to proposal | After years of sweet romance, tonight I will propose |
| 83 | **propose** (iamb) / **roses** (trochee) | assonance | same scene: romantic marriage proposal | I'll propose with a dozen roses in my hand |
| 84 | **cocoa** (trochee) / **cozy** (trochee) | assonance | same scene: warm winter evening | Cozy by the fire with a mug of cocoa |
| 85 | **coastline** (trochee) / **ocean** (trochee) | assonance | part/whole: shore of ocean | Along the coastline where the ocean meets the sky |
| 86 | **afloat** (iamb) / **boating** (trochee) | assonance | same scene: drifting lake boat | Lazy summer boating, we are drifting soft afloat |
| 87 | **moment** (trochee) / **photo** (trochee) | assonance | part/whole: snapshot of moment | Hold this moment in a photo, frame it on the wall |
| 88 | **nouveau** (iamb) / **baroque** (iamb) | assonance | same domain: art history styles | From art nouveau to baroque, the gallery glows with gold |
| 89 | **cologne** (iamb) / **lotion** (trochee) | assonance | same domain: scented grooming products | A touch of cologne and a little lotion before the dance |
| 90 | **yoga** (trochee) / **lotus** (trochee) | assonance | same domain: meditation pose practice | Morning yoga in the lotus pose beneath the sun |
| 91 | **protein** (trochee) / **tofu** (trochee) | assonance | same domain: plant-based nutrition | A bowl of tofu packed with protein and with love |
| 92 | **invoke** (iamb) / **holy** (trochee) | assonance | same domain: sacred prayer words | We invoke the holy light to guide us home |
| 93 | **frozen** (trochee) / **snowy** (trochee) | assonance | same scene: winter wonderland hills | Frozen lakes and snowy hills, a winter wonderland |
| 94 | **snowflake** (trochee) / **frozen** (trochee) | assonance | same scene: icy winter window | A single snowflake on a frozen windowpane |
| 95 | **lotus** (trochee) / **floating** (trochee) | assonance | same scene: pond blossoms drifting | A pink lotus floating on the quiet pond |
| 96 | **smoky** (trochee) / **roasted** (trochee) | assonance | same scene: campfire cookout night | Smoky embers glow while marshmallows are roasted |
| 97 | **plateau** (iamb) / **sloping** (trochee) | assonance | same scene: mountain terrain hike | Past the sloping hills we reach the wide plateau |
| 98 | **robot** (trochee) / **program** (trochee) | assonance | same domain: machine coding work | My little robot runs a program made of dreams |
| 99 | **slogan** (trochee) / **logo** (trochee) | assonance | same domain: brand identity design | A bright new logo and a slogan full of cheer |
| 100 | **donut** (trochee) / **cocoa** (trochee) | assonance | same scene: cafe breakfast treat | A sugar donut and a cup of cocoa at dawn |

**Near-misses rejected (Long O)**

1. **golden / glowing** — Golden fails the rules because its long O is l-controlled (the L closes the syllable before D).
2. **cologne / perfume** — Perfume is r-controlled (CMU has ER0 before F), so it can't be a partner even though the meaning fits.
3. **grocery / produce** — Grocery fails meter because CMU also lists a three-syllable gro-ce-ry pronunciation, which makes its meter ambiguous.
4. **going / staying** — The slant comes only from the -ing suffix, since the stems go and stay share no sounds.
5. **only / lonely** — Lonely is a sad, negative word, and both words come from the same one/lone root.

## Long U

/uː/, /juː/ as in *music, balloon* — CMU `UW` under primary stress.

| # | Pair | Rhyme type | Relationship | One-line example use |
|---|---|---|---|---|
| 1 | **beauty** (trochee) / **cutie** (trochee) | perfect | synonyms: lovely darling charm | You're my beauty and my cutie in the morning sun |
| 2 | **blooming** (trochee) / **booming** (trochee) | perfect | synonyms: thriving and flourishing | The roses are blooming and the laughter is booming |
| 3 | **smoothing** (trochee) / **soothing** (trochee) | perfect | synonyms: gentle calming touch | Smoothing back your hair with a soothing lullaby |
| 4 | **acute** (iamb) / **astute** (iamb) | perfect | synonyms: sharp keen insight | With an acute eye and an astute heart you find the light |
| 5 | **beauty** (trochee) / **duty** (trochee) | perfect | antonyms: pleasure versus obligation | I set my duty down to wander in the beauty |
| 6 | **conclude** (iamb) / **debuted** (iamb) | perfect | antonyms: beginning versus ending | Our song debuted at dawn and will conclude beneath the stars |
| 7 | **truly** (trochee) / **duly** (trochee) | perfect | synonyms: rightly and sincerely | Duly promised, truly yours, forever and a day |
| 8 | **debut** (iamb) / **anew** (iamb) | perfect | synonyms: fresh new beginning | Every sunrise is a debut, so let's begin anew |
| 9 | **truly** (trochee) / **newly** (trochee) | perfect | same scene: wedding day vows | Newly wed and truly in love tonight |
| 10 | **lagoon** (iamb) / **monsoon** (iamb) | perfect | same scene: tropical rainy season | The monsoon sings its rhythm on the blue lagoon |
| 11 | **movie** (trochee) / **groovy** (trochee) | perfect | same scene: retro film night | A groovy movie and a bowl of buttered popcorn |
| 12 | **debut** (iamb) / **revue** (iamb) | perfect | same domain: stage show premiere | Her bright debut lit up the summer revue |
| 13 | **student** (trochee) / **prudent** (trochee) | perfect | same domain: wise young learner | A prudent student keeps her lantern burning |
| 14 | **acute** (iamb) / **minute** (iamb) | perfect | same domain: fine sharp precision | With acute attention to each minute detail |
| 15 | **review** (iamb) / **debut** (iamb) | perfect | same domain: critics greet premiere | The papers review your debut with shining praise |
| 16 | **canoe** (iamb) / **bamboo** (iamb) | perfect | same scene: jungle river paddle | A bamboo paddle guides our little green canoe |
| 17 | **raccoon** (iamb) / **lagoon** (iamb) | perfect | same scene: moonlit wildlife pond | A curious raccoon dips its paws in the lagoon |
| 18 | **reboot** (iamb) / **compute** (iamb) | perfect | same domain: computer restart task | Reboot the screen and compute a brighter plan |
| 19 | **recruit** (iamb) / **salute** (iamb) | perfect | same scene: proud parade ground | The proud recruit gives a crisp salute |
| 20 | **costume** (iamb) / **assume** (iamb) | perfect | cause/effect: costume assumes role | Assume a hero's role in a velvet costume |
| 21 | **tuning** (trochee) / **pruning** (trochee) | perfect | same domain: careful fine refining | Pruning the roses and tuning my guitar |
| 22 | **grooming** (trochee) / **pruning** (trochee) | slant | synonyms: trimming and tending | Pruning the hedges is grooming the garden green |
| 23 | **blooming** (trochee) / **pruning** (trochee) | slant | same scene: spring garden care | Pruning the branches while the lilacs are blooming |
| 24 | **moving** (trochee) / **soothing** (trochee) | slant | same domain: tender heartfelt music | Your song is moving and your voice is soothing |
| 25 | **fruity** (trochee) / **foodie** (trochee) | slant | same domain: flavor lover's delight | A fruity tart for the foodie in your heart |
| 26 | **juicy** (trochee) / **sushi** (trochee) | slant | same scene: tasty dinner treat | Juicy mango rolls beside the sushi plate |
| 27 | **compute** (iamb) / **conclude** (iamb) | slant | same domain: logical reasoning steps | We compute the clues and conclude with a smile |
| 28 | **recruit** (iamb) / **include** (iamb) | slant | same domain: welcoming new members | Recruit the dreamers and include the shy ones too |
| 29 | **costume** (iamb) / **balloon** (iamb) | slant | same scene: costume party fun | A clown costume and a bright red balloon |
| 30 | **booming** (trochee) / **tuning** (trochee) | slant | same scene: concert sound check | Tuning up the strings while the drums are booming |
| 31 | **moving** (trochee) / **proving** (trochee) | perfect | same domain: steady forward progress | Keep on moving, keep on proving what you are |
| 32 | **rooted** (trochee) / **suited** (trochee) | perfect | same domain: settled and belonging | Deeply rooted and well suited to this land |
| 33 | **cutie** (trochee) / **sweetie** (trochee) | slant | synonyms: darling dear one | Come here, sweetie, you're my little cutie |
| 34 | **cutie** (trochee) / **pretty** (trochee) | slant | synonyms: adorable and lovely | You're a pretty little cutie with a sunny smile |
| 35 | **minute** (iamb) / **petite** (iamb) | slant | synonyms: tiny and small | A minute, petite little flower in the dew |
| 36 | **approve** (iamb) / **believe** (iamb) | slant | synonyms: affirm and trust | I believe in you and I approve of every dream |
| 37 | **conclude** (iamb) / **decide** (iamb) | slant | synonyms: settle the matter | We decide to dance and conclude the night with song |
| 38 | **improve** (iamb) / **revive** (iamb) | slant | synonyms: restore and refresh | Spring rain will revive the fields and improve the day |
| 39 | **improve** (iamb) / **achieve** (iamb) | slant | cause/effect: growth brings success | Improve a little every day and you'll achieve your dream |
| 40 | **recruit** (iamb) / **cadet** (iamb) | slant | synonyms: new young trainee | The new recruit and the young cadet march side by side |
| 41 | **suited** (trochee) / **fitted** (trochee) | slant | synonyms: tailored to fit | A fitted coat that's perfectly suited to you |
| 42 | **astute** (iamb) / **discreet** (iamb) | slant | synonyms: wise and tactful | An astute friend is gentle and discreet |
| 43 | **juicy** (trochee) / **spicy** (trochee) | slant | same domain: bold tasty flavors | Juicy peaches and a spicy cup of tea |
| 44 | **reboot** (iamb) / **update** (iamb) | slant | same domain: system refresh routine | Update your heart and reboot your smile |
| 45 | **lagoon** (iamb) / **serene** (iamb) | slant | same scene: calm tropical water | The lagoon lies serene beneath the swaying palms |
| 46 | **moving** (trochee) / **loving** (trochee) | slant | same domain: tender heartfelt emotion | A moving song to fill a loving heart |
| 47 | **soothing** (trochee) / **breathing** (trochee) | slant | same scene: calm meditation time | Slow breathing and a soothing tune at dusk |
| 48 | **proving** (trochee) / **striving** (trochee) | slant | cause/effect: effort proves worth | Striving every day and proving what we can do |
| 49 | **commute** (iamb) / **remote** (iamb) | slant | antonyms: office versus home | I traded the commute for a remote and sunny view |
| 50 | **proven** (trochee) / **given** (trochee) | slant | same domain: certain settled truths | Your kindness is proven and your love is a given |
| 51 | **include** (iamb) / **provide** (iamb) | slant | same domain: sharing and giving | Provide a chair and include everyone tonight |
| 52 | **cocoon** (iamb) / **begin** (iamb) | slant | cause/effect: new wings begin | Inside the cocoon the brand new wings begin |
| 53 | **costume** (iamb) / **become** (iamb) | slant | cause/effect: costume transforms wearer | Put on the costume and become the star |
| 54 | **cruising** (trochee) / **gazing** (trochee) | slant | same scene: scenic open drive | Cruising down the coast and gazing at the sea |
| 55 | **commune** (iamb) / **serene** (iamb) | slant | same scene: peaceful nature retreat | We commune with the forest, quiet and serene |
| 56 | **raccoon** (iamb) / **ravine** (iamb) | slant | same scene: woodland creek night | A raccoon wanders down the misty ravine |
| 57 | **juicy** (trochee) / **fruity** (trochee) | assonance | synonyms: luscious ripe flavor | Juicy plums and fruity wine at sunset |
| 58 | **astute** (iamb) / **prudent** (trochee) | assonance | synonyms: wise sound judgment | An astute and prudent heart will guide the way |
| 59 | **truly** (trochee) / **proven** (trochee) | assonance | synonyms: certain and genuine | Your kindness is truly proven every day |
| 60 | **lucid** (trochee) / **fluent** (trochee) | assonance | synonyms: clear smooth expression | Lucid dreams and fluent songs of hope |
| 61 | **boosted** (trochee) / **improved** (iamb) | assonance | synonyms: lifted and upgraded | Your kindness boosted me and improved my day |
| 62 | **juices** (trochee) / **fruity** (trochee) | assonance | same domain: fresh fruit drinks | Morning juices, fruity, sweet, and bright |
| 63 | **renew** (iamb) / **improve** (iamb) | assonance | synonyms: refresh and better | Renew your hope and improve your little world |
| 64 | **ruby** (trochee) / **maroon** (iamb) | assonance | synonyms: deep red shades | A ruby sunset slowly fading to maroon |
| 65 | **loosely** (trochee) / **smoothly** (trochee) | assonance | synonyms: easy flowing motion | Swaying loosely, gliding smoothly through the night |
| 66 | **fluid** (trochee) / **smoothly** (trochee) | assonance | synonyms: flowing and graceful | Fluid steps and smoothly turning feet |
| 67 | **smoothing** (trochee) / **grooming** (trochee) | assonance | synonyms: tidying with care | Smoothing her mane and grooming the pony |
| 68 | **include** (iamb) / **unite** (trochee) | assonance | synonyms: bring people together | Unite the neighbors and include us all |
| 69 | **commune** (iamb) / **unite** (trochee) | assonance | synonyms: come together peacefully | We unite in song and commune beneath the stars |
| 70 | **duo** (trochee) / **union** (trochee) | assonance | synonyms: joined loving pair | A duo in a happy union, hand in hand |
| 71 | **kudos** (trochee) / **salute** (iamb) | assonance | synonyms: praise and honor | Kudos to the dreamers and a salute to the brave |
| 72 | **groovy** (trochee) / **boogie** (trochee) | assonance | same scene: disco dance floor | Put on something groovy and boogie all night long |
| 73 | **music** (trochee) / **tuning** (trochee) | assonance | same domain: musical preparation work | Tuning my heart to the music of you |
| 74 | **bluegrass** (trochee) / **music** (trochee) | assonance | part/whole: genre of music | Bluegrass music drifting through the hills |
| 75 | **sushi** (trochee) / **tuna** (trochee) | assonance | part/whole: fish in sushi | Fresh tuna rolled into sushi for two |
| 76 | **sushi** (trochee) / **foodie** (trochee) | assonance | same domain: food lover favorite | Every foodie dreams of sushi by the sea |
| 77 | **music** (trochee) / **movie** (trochee) | assonance | same domain: entertainment arts | The music in the movie made my heart take flight |
| 78 | **cocoon** (iamb) / **renewed** (iamb) | assonance | cause/effect: change brings renewal | Out of the cocoon, my wings renewed |
| 79 | **reviewed** (iamb) / **approved** (iamb) | assonance | same domain: evaluation and acceptance | Reviewed with care and approved with a smile |
| 80 | **kudos** (trochee) / **approve** (iamb) | assonance | same domain: praise and approval | I approve, and kudos for your courage |
| 81 | **student** (trochee) / **fluent** (trochee) | assonance | cause/effect: study brings fluency | A student growing fluent in a brand new tongue |
| 82 | **roommate** (trochee) / **student** (trochee) | assonance | same scene: college dorm life | My roommate is a student of the stars |
| 83 | **boosting** (trochee) / **booming** (trochee) | assonance | same domain: rising growth surge | Boosting every dream while the city's booming |
| 84 | **amused** (iamb) / **goofy** (trochee) | assonance | cause/effect: silliness brings laughter | Your goofy grin keeps me amused all day |
| 85 | **goofy** (trochee) / **boogie** (trochee) | assonance | same scene: silly kitchen dance | Let us do a goofy boogie in the kitchen |
| 86 | **hula** (trochee) / **bamboo** (iamb) | assonance | same scene: island luau night | We hula by the bamboo torches on the shore |
| 87 | **hula** (trochee) / **tutu** (trochee) | assonance | same domain: swaying dance skirts | From a hula skirt to a ballet tutu, we dance |
| 88 | **boogie** (trochee) / **jukebox** (trochee) | assonance | same scene: retro diner dance | Drop a coin in the jukebox and boogie down |
| 89 | **moonlight** (trochee) / **canoe** (iamb) | assonance | same scene: night river paddle | Paddle the canoe through silver moonlight |
| 90 | **rooftop** (trochee) / **moonlight** (trochee) | assonance | same scene: night city view | Dancing on the rooftop in the moonlight |
| 91 | **blooming** (trochee) / **tulip** (trochee) | assonance | same scene: spring garden bed | Every tulip blooming in the April sun |
| 92 | **tulip** (trochee) / **ruby** (trochee) | assonance | same scene: red spring blooms | A ruby tulip opening at dawn |
| 93 | **humid** (trochee) / **monsoon** (iamb) | assonance | same scene: tropical wet season | Humid air before the monsoon sings |
| 94 | **shampoo** (iamb) / **grooming** (trochee) | assonance | same domain: personal care routine | A little shampoo and some grooming for the show |
| 95 | **toothpaste** (trochee) / **shampoo** (iamb) | assonance | same scene: bathroom morning shelf | Toothpaste, shampoo, and a song in the shower |
| 96 | **movie** (trochee) / **viewing** (trochee) | assonance | same scene: cozy film night | Viewing a movie curled up by the fire |
| 97 | **suitcase** (trochee) / **cruises** (trochee) | assonance | same scene: vacation travel trip | Pack a suitcase for the summer cruises |
| 98 | **smoothly** (trochee) / **cruising** (trochee) | assonance | same scene: easy open road | Cruising smoothly down the open road |
| 99 | **scuba** (trochee) / **tuna** (trochee) | assonance | same scene: ocean dive adventure | Scuba diving with the silver tuna |
| 100 | **tubing** (trochee) / **canoe** (iamb) | assonance | same scene: lazy river day | Tubing down the river beside a red canoe |

**Near-misses rejected (Long U)**

1. **renew / anew** — A perfect rhyme with a tight meaning, but both words are built on the root "new", so it is repetition rather than rhyme.
2. **viewing / seeing** — Strong synonyms, but after the different stressed vowels the only shared sound is the -ing suffix, so the link does not come from the stems.
3. **student / tutor** — A perfect classroom pairing in meaning, but tutor ends in an r-controlled ER syllable.
4. **balloon / afternoon** — Same summer-party scene and a full rhyme, but afternoon has three syllables, so it fails the two-syllable iamb/trochee meter.
5. **lagoon / typhoon** — A perfect rhyme in the same tropical scene, but typhoon calls up a destructive storm rather than a positive image.

## Short A

/æ/ as in *happy, gladly* — CMU `AE` under primary stress.

| # | Pair | Rhyme type | Relationship | One-line example use |
|---|---|---|---|---|
| 1 | **advance** (iamb) / **enhance** (iamb) | perfect | synonyms: progress and improve | With every step we advance, every dream we enhance |
| 2 | **crafted** (trochee) / **drafted** (trochee) | perfect | synonyms: designed with care | Every verse I drafted, every chorus crafted just for you |
| 3 | **banish** (trochee) / **vanish** (trochee) | perfect | synonyms: make worries disappear | Banish all the gray clouds and watch the worries vanish |
| 4 | **exact** (iamb) / **abstract** (iamb) | perfect | antonyms: precise versus vague | Love isn't something abstract, it's exact as the sunrise |
| 5 | **happy** (trochee) / **snappy** (trochee) | perfect | synonyms: cheerful lively mood | Keep it happy, keep it snappy, let the rhythm roll |
| 6 | **baggy** (trochee) / **shaggy** (trochee) | perfect | synonyms: loose and scruffy | Baggy sweater, shaggy hair, and a carefree Sunday grin |
| 7 | **packing** (trochee) / **stacking** (trochee) | perfect | synonyms: loading up boxes | Packing up our memories and stacking them with care |
| 8 | **gladly** (trochee) / **madly** (trochee) | perfect | synonyms: eager wholehearted love | I would gladly fall for you, madly and for good |
| 9 | **handy** (trochee) / **dandy** (trochee) | perfect | synonyms: useful and fine | With a handy little tune the day is fine and dandy |
| 10 | **compact** (iamb) / **intact** (iamb) | perfect | synonyms: snug and whole | Fold the dream up compact and carry it intact |
| 11 | **glances** (trochee) / **dances** (trochee) | perfect | same scene: ballroom flirtation | Stolen glances turned to slow dances under the stars |
| 12 | **action** (trochee) / **traction** (trochee) | perfect | cause/effect: effort gains momentum | Put your dreams in action and they'll find their traction |
| 13 | **fashion** (trochee) / **passion** (trochee) | perfect | same domain: love of style | She stitched her passion into fashion made of gold |
| 14 | **clapping** (trochee) / **tapping** (trochee) | perfect | same scene: keeping the beat | Hands are clapping, feet are tapping to the band |
| 15 | **glances** (trochee) / **chances** (trochee) | perfect | cause/effect: glance sparks chance | Second glances turn to second chances |
| 16 | **classes** (trochee) / **passes** (trochee) | perfect | cause/effect: study earns success | She smiles and passes all her classes with ease |
| 17 | **dancing** (trochee) / **glancing** (trochee) | perfect | same scene: moonlit dance floor | Dancing in the moonlight, glancing at your smile |
| 18 | **lashes** (trochee) / **flashes** (trochee) | perfect | same scene: bright flirting eyes | Her lashes flutter every time the camera flashes |
| 19 | **granny** (trochee) / **nanny** (trochee) | perfect | same domain: loving childhood caregivers | Granny bakes the cookies while the nanny sings along |
| 20 | **classy** (trochee) / **sassy** (trochee) | perfect | same domain: confident stylish attitude | She's classy in the morning and sassy on the dance floor |
| 21 | **mango** (trochee) / **tango** (trochee) | perfect | same scene: tropical summer dance | Sweet mango on our lips, we tango through the night |
| 22 | **planet** (trochee) / **granite** (trochee) | perfect | part/whole: rock of planet | This planet's made of granite and a million dreams |
| 23 | **napping** (trochee) / **tapping** (trochee) | perfect | same scene: rainy afternoon rest | Napping on the sofa while the rain is softly tapping |
| 24 | **landing** (trochee) / **standing** (trochee) | perfect | cause/effect: landing earns ovation | She stuck the landing and the crowd was standing |
| 25 | **romance** (iamb) / **expanse** (iamb) | perfect | same scene: starlit open sky | Romance beneath the wide expanse of stars |
| 26 | **splashing** (trochee) / **flashing** (trochee) | perfect | same scene: sunlit summer water | Children splashing in the lake with silver ripples flashing |
| 27 | **grasses** (trochee) / **passes** (trochee) | perfect | same scene: breeze through meadow | The summer wind passes softly through the grasses |
| 28 | **tanning** (trochee) / **fanning** (trochee) | perfect | same scene: summer beach heat | Tanning on the sand while the palm leaves keep on fanning |
| 29 | **clapping** (trochee) / **snapping** (trochee) | perfect | same scene: rhythm of hands | Fingers snapping, palms clapping, everybody sing |
| 30 | **splashing** (trochee) / **dashing** (trochee) | perfect | same scene: running through surf | Dashing through the waves and splashing in the sun |
| 31 | **napping** (trochee) / **wrapping** (trochee) | perfect | same scene: cozy blanket nap | Napping by the fire, wrapping up in wool |
| 32 | **flashing** (trochee) / **dashing** (trochee) | perfect | same scene: charming bright smile | A dashing grin and flashing eyes across the room |
| 33 | **spanning** (trochee) / **scanning** (trochee) | perfect | same scene: wide horizon view | Scanning the horizon with a rainbow spanning wide |
| 34 | **sandy** (trochee) / **candy** (trochee) | perfect | same scene: seaside boardwalk treats | Sandy toes and cotton candy on the pier |
| 35 | **exact** (iamb) / **correct** (iamb) | slant | synonyms: precise and right | Every word exact, every note correct |
| 36 | **impact** (iamb) / **effect** (iamb) | slant | synonyms: lasting influence result | Your kindness made an impact with a gentle, lasting effect |
| 37 | **expanse** (iamb) / **immense** (iamb) | slant | synonyms: vast open space | The ocean's blue expanse is immense and free |
| 38 | **classy** (trochee) / **flashy** (trochee) | slant | antonyms: refined versus showy | She's classy, never flashy, shining soft and true |
| 39 | **granted** (trochee) / **handed** (trochee) | slant | synonyms: given as gift | Every wish was granted, every star was handed down |
| 40 | **subtract** (iamb) / **deduct** (iamb) | slant | synonyms: take away amounts | Subtract the doubt and deduct the fear tonight |
| 41 | **dandy** (trochee) / **trendy** (trochee) | slant | synonyms: stylish sharp dresser | Dressed up like a dandy, looking trendy on the town |
| 42 | **react** (iamb) / **reflect** (iamb) | slant | antonyms: impulse versus thought | Don't react too quickly, take a breath and reflect |
| 43 | **expand** (iamb) / **ascend** (iamb) | slant | synonyms: growing and rising | Let your heart expand as the morning larks ascend |
| 44 | **action** (trochee) / **fiction** (trochee) | slant | antonyms: doing versus dreaming | Turn the pages of your fiction into action |
| 45 | **classy** (trochee) / **jazzy** (trochee) | slant | same domain: stylish lively flair | A classy little club with a jazzy band till dawn |
| 46 | **sassy** (trochee) / **jazzy** (trochee) | slant | same domain: bold lively style | She's sassy when she sings a jazzy melody |
| 47 | **fashion** (trochee) / **flashing** (trochee) | slant | same scene: runway camera lights | Cameras flashing as the fashion parade goes by |
| 48 | **grasses** (trochee) / **flashes** (trochee) | slant | same scene: firefly summer meadow | Fireflies in the grasses throwing tiny golden flashes |
| 49 | **cabin** (trochee) / **snapping** (trochee) | slant | same scene: crackling cozy fire | The fire is snapping in our little cabin |
| 50 | **camping** (trochee) / **chanting** (trochee) | slant | same scene: campfire singalong night | Camping by the lake and chanting songs beneath the moon |
| 51 | **standing** (trochee) / **chanting** (trochee) | slant | same scene: cheering stadium crowd | The crowd is standing, chanting out your name |
| 52 | **baggy** (trochee) / **khaki** (trochee) | slant | same scene: casual weekend clothes | Baggy khaki trousers on a lazy Sunday stroll |
| 53 | **dancing** (trochee) / **mansion** (trochee) | slant | same scene: grand ballroom party | We were dancing in the mansion till the morning light |
| 54 | **glancing** (trochee) / **handsome** (trochee) | slant | same scene: shy admiring look | Glancing at a handsome stranger by the door |
| 55 | **branches** (trochee) / **benches** (trochee) | slant | same scene: shady city park | Sunlight through the branches on the old park benches |
| 56 | **satin** (trochee) / **wrapping** (trochee) | slant | same scene: elegant gift ribbon | Satin ribbon wrapping every present with a bow |
| 57 | **packing** (trochee) / **wagon** (trochee) | slant | same scene: pioneer road trip | Packing up the wagon for the long road west |
| 58 | **romance** (iamb) / **commence** (iamb) | slant | same scene: love story begins | Let the music play and let the romance commence |
| 59 | **active** (trochee) / **passive** (trochee) | assonance | antonyms: busy versus still | Some days I'm active, some days passive as the sea |
| 60 | **rapid** (trochee) / **placid** (trochee) | assonance | antonyms: rushing versus calm | From rapid mountain rivers to the placid lake below |
| 61 | **contract** (iamb) / **expand** (iamb) | assonance | antonyms: shrink versus grow | Our hearts contract and then expand with every breath |
| 62 | **advance** (iamb) / **retract** (iamb) | assonance | antonyms: forward versus back | The waves advance and then retract along the shore |
| 63 | **mansion** (trochee) / **cabin** (trochee) | assonance | antonyms: grand versus humble | I'd trade a marble mansion for a cabin by the lake |
| 64 | **passage** (trochee) / **pathway** (trochee) | assonance | synonyms: a way through | A hidden passage opens to a sunlit pathway |
| 65 | **savvy** (trochee) / **crafty** (trochee) | assonance | synonyms: shrewd and clever | She's savvy with her money and crafty with her hands |
| 66 | **handsome** (trochee) / **dashing** (trochee) | assonance | synonyms: attractive charming gentleman | So handsome and so dashing in his Sunday suit |
| 67 | **lavish** (trochee) / **fancy** (trochee) | assonance | synonyms: rich and elegant | A fancy gown, a lavish ball, a night to remember |
| 68 | **practice** (trochee) / **habit** (trochee) | assonance | synonyms: steady daily routine | Make your practice a habit and the music comes alive |
| 69 | **mapping** (trochee) / **planning** (trochee) | assonance | synonyms: plotting the route | Mapping out the journey, planning every stop |
| 70 | **happy** (trochee) / **gladly** (trochee) | assonance | synonyms: joyful and willing | I'm happy and I'll gladly sing along with you |
| 71 | **catchy** (trochee) / **snappy** (trochee) | assonance | synonyms: lively memorable tune | A catchy little chorus with a snappy little beat |
| 72 | **happy** (trochee) / **laughing** (trochee) | assonance | cause/effect: joy brings laughter | We were happy, we were laughing till the dawn |
| 73 | **magnet** (trochee) / **attract** (iamb) | assonance | cause/effect: magnet draws close | You're a magnet and you attract the morning sun |
| 74 | **antics** (trochee) / **laughing** (trochee) | assonance | cause/effect: silliness brings laughter | Your silly little antics keep me laughing all day |
| 75 | **pastime** (trochee) / **passion** (trochee) | assonance | synonyms: hobby and love | My favorite pastime turned into my passion |
| 76 | **fabric** (trochee) / **fashion** (trochee) | assonance | part/whole: fabric makes fashion | Turning silky fabric into fashion for the stage |
| 77 | **tango** (trochee) / **dancing** (trochee) | assonance | part/whole: tango within dancing | Dancing the tango underneath the city lights |
| 78 | **package** (trochee) / **wrapping** (trochee) | assonance | part/whole: package in wrapping | Tearing off the wrapping on a package full of love |
| 79 | **aspen** (trochee) / **branches** (trochee) | assonance | part/whole: branches of aspen | Golden aspen branches swaying in the breeze |
| 80 | **blanket** (trochee) / **basket** (trochee) | assonance | same scene: picnic spread | Spread the blanket, open up the basket |
| 81 | **magic** (trochee) / **rabbit** (trochee) | assonance | same scene: magician's hat trick | A little bit of magic pulls a rabbit from the hat |
| 82 | **hammock** (trochee) / **napping** (trochee) | assonance | same scene: lazy summer afternoon | Napping in the hammock while the summer breezes blow |
| 83 | **angling** (trochee) / **casting** (trochee) | assonance | same scene: fishing by river | Angling by the river, casting lines into the light |
| 84 | **canvas** (trochee) / **landscape** (trochee) | assonance | same scene: painting outdoors | She paints a golden landscape on a canvas by the sea |
| 85 | **cactus** (trochee) / **canyon** (trochee) | assonance | same scene: desert sunset | A lonely cactus glowing in the canyon light |
| 86 | **snapshot** (trochee) / **candid** (trochee) | assonance | same scene: natural photo moment | A candid little snapshot of the summer that we shared |
| 87 | **statue** (trochee) / **plaza** (trochee) | assonance | same scene: sunny town square | We met beside the statue in the plaza |
| 88 | **relax** (iamb) / **unpack** (iamb) | assonance | same scene: vacation arrival | Unpack the bags and relax beside the sea |
| 89 | **bathtub** (trochee) / **splashing** (trochee) | assonance | same scene: bubbly bath time | Splashing in the bathtub, bubbles everywhere |
| 90 | **mattress** (trochee) / **blanket** (trochee) | assonance | same scene: cozy bed | A feather mattress and a woolen blanket |
| 91 | **sandwich** (trochee) / **napkin** (trochee) | assonance | same scene: picnic lunch | A sandwich and a napkin on a sunny afternoon |
| 92 | **lavish** (trochee) / **banquet** (trochee) | assonance | same scene: grand feast | A lavish banquet laid beneath the stars |
| 93 | **banjo** (trochee) / **jamming** (trochee) | assonance | same scene: porch music jam | Jamming on the banjo on the porch at night |
| 94 | **gadget** (trochee) / **handy** (trochee) | assonance | same domain: useful little tools | A handy little gadget in my pocket for the road |
| 95 | **laughing** (trochee) / **chatting** (trochee) | assonance | same scene: friends together | Laughing and chatting till the stars come out |
| 96 | **athlete** (trochee) / **practice** (trochee) | assonance | same scene: daily training | An athlete knows that practice builds the dream |
| 97 | **campus** (trochee) / **classes** (trochee) | assonance | same scene: college life | Walking through the campus to our morning classes |
| 98 | **campsite** (trochee) / **backpack** (trochee) | assonance | same scene: camping trip | Drop the backpack at the campsite by the stream |
| 99 | **grassland** (trochee) / **rabbit** (trochee) | assonance | same scene: open meadow | A rabbit hopping softly through the grassland |
| 100 | **mantra** (trochee) / **chanting** (trochee) | assonance | same scene: peaceful morning meditation | Chanting our mantra as the morning light arrives |

**Near-misses rejected (Short A)**

1. **magic / tragic** — A perfect rhyme, but tragic is a grim, negative word, so the pair breaks the positivity rule.
2. **laughter / after** — Both words end in an r-controlled -er syllable, which the sound rules forbid.
3. **rambling / scrambling** — A strong synonym rhyme, but CMU also gives a three-syllable reading (ram-bl-ing), so the two-syllable meter is ambiguous and the words are disqualified.
4. **passion / potion** — The stressed vowels differ, so the only shared sound is the -tion/-sion suffix ending, not the stems.
5. **attached / detached** — The two words share the root tach, so this is repetition with a swapped prefix, not a rhyme.

## Short E

/ɛ/ as in *festive, blessing* — CMU `EH` under primary stress.

| # | Pair | Rhyme type | Relationship | One-line example use |
|---|---|---|---|---|
| 1 | **ready** (trochee) / **steady** (trochee) | perfect | synonyms: prepared and firm | Hold me ready, hold me steady, through the night |
| 2 | **intense** (iamb) / **immense** (iamb) | perfect | synonyms: vast and powerful | A love intense, a sky immense above us |
| 3 | **many** (trochee) / **plenty** (trochee) | perfect | synonyms: more than enough | So many stars and plenty more to wish upon |
| 4 | **sketching** (trochee) / **etching** (trochee) | perfect | synonyms: drawing fine lines | Sketching your smile and etching it in gold |
| 5 | **detect** (iamb) / **inspect** (iamb) | perfect | synonyms: notice and examine | Inspect the night and you'll detect a falling star |
| 6 | **success** (iamb) / **progress** (iamb) | perfect | synonyms: moving forward, achieving | Every bit of progress lifts us to success |
| 7 | **express** (iamb) / **confess** (iamb) | perfect | synonyms: voicing true feelings | Let me confess the words I long to express |
| 8 | **request** (iamb) / **suggest** (iamb) | perfect | synonyms: politely proposing ideas | May I suggest a song, may I request a dance |
| 9 | **ascend** (iamb) / **extend** (iamb) | perfect | synonyms: reaching ever higher | Extend your wings and ascend into the blue |
| 10 | **eddy** (trochee) / **steady** (trochee) | perfect | antonyms: swirling versus still | The river eddy spins, but my heart holds steady |
| 11 | **penny** (trochee) / **plenty** (trochee) | perfect | antonyms: scarce versus abundant | From a single penny grew a life of plenty |
| 12 | **testing** (trochee) / **resting** (trochee) | perfect | antonyms: effort versus ease | After testing days, my happy heart is resting |
| 13 | **heaven** (trochee) / **haven** (trochee) | slant | synonyms: safe sanctuary | Your arms are my haven, your kiss a taste of heaven |
| 14 | **friendly** (trochee) / **gently** (trochee) | slant | synonyms: kind and soft | A friendly voice that speaks to me so gently |
| 15 | **friendly** (trochee) / **kindly** (trochee) | slant | synonyms: warm and caring | A friendly wave, a kindly word, a sunny day |
| 16 | **heaven** (trochee) / **seven** (trochee) | perfect | same scene: seventh heaven bliss | Seven stars above us shine like heaven tonight |
| 17 | **menu** (trochee) / **venue** (trochee) | perfect | same scene: dinner date night | A candlelit venue and a menu made for two |
| 18 | **question** (trochee) / **session** (trochee) | perfect | same scene: classroom discussion | Every question in the session sparks a light |
| 19 | **duet** (iamb) / **cassette** (iamb) | perfect | same scene: music recording | We sang a sweet duet on an old cassette |
| 20 | **rested** (trochee) / **nested** (trochee) | perfect | same scene: birds at home | The swallows rested where they nested in the eaves |
| 21 | **resting** (trochee) / **nesting** (trochee) | perfect | same scene: spring birds settling | Doves are resting, robins nesting in the pines |
| 22 | **respect** (iamb) / **protect** (iamb) | perfect | cause/effect: respect inspires protection | I respect your heart and I'll protect it always |
| 23 | **finesse** (iamb) / **impress** (iamb) | perfect | cause/effect: skill wins admiration | Dance with finesse and you will impress the crowd |
| 24 | **penny** (trochee) / **money** (trochee) | slant | part/whole: coin of money | Every penny saved is money for our dreams |
| 25 | **precious** (trochee) / **gracious** (trochee) | slant | synonyms: dear and kind | So precious and so gracious is your love |
| 26 | **empty** (trochee) / **plenty** (trochee) | slant | antonyms: none versus abundance | Empty hands are filling up with plenty |
| 27 | **steady** (trochee) / **speedy** (trochee) | slant | antonyms: slow versus fast | Not speedy, just steady, I will win the race |
| 28 | **respite** (trochee) / **rested** (trochee) | slant | synonyms: pause and rest | A gentle respite, and my soul has rested |
| 29 | **reflect** (iamb) / **project** (iamb) | perfect | same domain: casting light outward | The moon will project what the lake will reflect |
| 30 | **collect** (iamb) / **reflect** (iamb) | perfect | same scene: quiet thoughtful moment | Collect your thoughts and reflect beneath the stars |
| 31 | **pleasant** (trochee) / **present** (trochee) | perfect | same scene: pleasant gift giving | A pleasant present wrapped in ribbons bright |
| 32 | **pheasant** (trochee) / **pleasant** (trochee) | perfect | same scene: country morning walk | A pleasant morning and a pheasant in the field |
| 33 | **entry** (trochee) / **sentry** (trochee) | perfect | same scene: guarded castle gate | A smiling sentry waves us through the entry |
| 34 | **suspense** (iamb) / **intense** (iamb) | perfect | same scene: thrilling story climax | The suspense is intense as the music swells |
| 35 | **commence** (iamb) / **suspense** (iamb) | perfect | same scene: curtain rising | Let the show commence, the sweet suspense is here |
| 36 | **blessing** (trochee) / **dressing** (trochee) | perfect | same scene: wedding morning | Dressing for the wedding, I count every blessing |
| 37 | **tending** (trochee) / **bending** (trochee) | perfect | same scene: gardener at work | Bending low and tending roses in the sun |
| 38 | **splendid** (trochee) / **tended** (trochee) | perfect | cause/effect: care makes beauty | The garden that she tended grew so splendid |
| 39 | **splendid** (trochee) / **blended** (trochee) | perfect | cause/effect: mixing creates beauty | The sunset colors blended into something splendid |
| 40 | **blending** (trochee) / **bending** (trochee) | perfect | same scene: prism splitting light | Bending light and blending colors through the glass |
| 41 | **edges** (trochee) / **hedges** (trochee) | perfect | same scene: garden borders | Roses climb along the edges of the hedges |
| 42 | **sketches** (trochee) / **stretches** (trochee) | perfect | same scene: landscape drawing | Sketches of the golden stretches of the shore |
| 43 | **connect** (iamb) / **respect** (iamb) | perfect | cause/effect: respect builds bonds | When we respect each other, we connect |
| 44 | **event** (iamb) / **present** (iamb) | perfect | same scene: presenting at gala | At the grand event we present our brand-new song |
| 45 | **lending** (trochee) / **sending** (trochee) | perfect | synonyms: giving help onward | Lending a hand and sending love your way |
| 46 | **invest** (iamb) / **progressed** (iamb) | perfect | cause/effect: effort brings growth | We invest our hearts and see how far we have progressed |
| 47 | **amen** (iamb) / **again** (iamb) | perfect | same scene: hymn refrain | Sing amen and sing it once again |
| 48 | **stretching** (trochee) / **reaching** (trochee) | slant | synonyms: extending outward | Stretching toward the sun and reaching for the sky |
| 49 | **finesse** (iamb) / **precise** (iamb) | slant | synonyms: skilled exactness | Precise and full of finesse, she paints the dawn |
| 50 | **connect** (iamb) / **attract** (iamb) | slant | synonyms: drawing together | Like magnets we attract, like stars we connect |
| 51 | **express** (iamb) / **release** (iamb) | slant | synonyms: letting feelings out | Release your fears and express your heart in song |
| 52 | **progress** (iamb) / **increase** (iamb) | slant | synonyms: steady growth | Watch our joys increase as we progress together |
| 53 | **defend** (iamb) / **withstand** (iamb) | slant | synonyms: holding firm | Together we withstand the wind and defend our dreams |
| 54 | **commence** (iamb) / **advance** (iamb) | slant | synonyms: start moving forward | Let the parade commence, let the dancers advance |
| 55 | **suggest** (iamb) / **insist** (iamb) | slant | antonyms: gentle versus firm | I suggest a walk, but you insist we dance |
| 56 | **lenses** (trochee) / **senses** (trochee) | slant | same domain: sight and perception | Through rosy lenses all my senses come alive |
| 57 | **message** (trochee) / **passage** (trochee) | slant | synonyms: shared written words | A passage in your letter holds a message bright |
| 58 | **lesson** (trochee) / **blessing** (trochee) | slant | cause/effect: lessons become blessings | Every lesson is a blessing in disguise |
| 59 | **meadow** (trochee) / **shadow** (trochee) | slant | same scene: shady summer field | Lie with me in the meadow, in the oak tree's shadow |
| 60 | **ready** (trochee) / **tidy** (trochee) | slant | same scene: neat and prepared | The room is tidy and I'm ready for you |
| 61 | **section** (trochee) / **fraction** (trochee) | slant | synonyms: part of whole | A tiny fraction, just a section of the pie |
| 62 | **request** (iamb) / **assist** (iamb) | slant | cause/effect: asking brings help | Just request a hand and I'll assist you |
| 63 | **protect** (iamb) / **intact** (iamb) | slant | cause/effect: guarding keeps whole | I'll protect your heart and keep it safe, intact |
| 64 | **intense** (iamb) / **romance** (iamb) | slant | same scene: passionate love | An intense romance beneath the summer moon |
| 65 | **event** (iamb) / **attend** (iamb) | slant | cause/effect: guests attend gatherings | We attend the grand event in our finest clothes |
| 66 | **duet** (iamb) / **delight** (iamb) | slant | cause/effect: harmony brings joy | Our duet rings out with pure delight |
| 67 | **cassette** (iamb) / **repeat** (iamb) | slant | same scene: tape on repeat | Our song on that cassette plays on repeat |
| 68 | **pleasant** (trochee) / **crescent** (trochee) | slant | same scene: evening crescent moon | A pleasant breeze beneath the crescent moon |
| 69 | **wedding** (trochee) / **setting** (trochee) | slant | same scene: wedding venue | A garden setting for our wedding day |
| 70 | **lesson** (trochee) / **session** (trochee) | slant | same scene: music class time | Our music lesson turned into a jam session |
| 71 | **possess** (iamb) / **embrace** (iamb) | slant | synonyms: holding close | Embrace me with the love that you possess |
| 72 | **address** (iamb) / **discuss** (iamb) | slant | synonyms: talking it through | Let's discuss our dreams and address each hope |
| 73 | **tested** (trochee) / **tasted** (trochee) | slant | same scene: chef's kitchen | We tasted and we tested every sweet recipe |
| 74 | **project** (iamb) / **construct** (iamb) | slant | same domain: building plans | We construct our dream, a project built with love |
| 75 | **splendid** (trochee) / **scented** (trochee) | slant | same scene: blooming rose garden | A splendid garden, scented by the rose |
| 76 | **bending** (trochee) / **winding** (trochee) | slant | same scene: river path | A winding river bending through the vale |
| 77 | **stepping** (trochee) / **skipping** (trochee) | slant | same scene: playful stroll | Stepping light and skipping down the lane |
| 78 | **epic** (trochee) / **legend** (trochee) | assonance | synonyms: grand heroic tale | An epic journey, a legend to be told |
| 79 | **destined** (trochee) / **legend** (trochee) | assonance | same theme: fated greatness | You were destined to become a legend in the light |
| 80 | **exit** (trochee) / **entrance** (trochee) | assonance | antonyms: leaving versus arriving | Every exit leads us to a brand-new entrance |
| 81 | **breakfast** (trochee) / **bedtime** (trochee) | assonance | antonyms: morning versus night | From breakfast kisses to bedtime lullabies |
| 82 | **rescue** (trochee) / **protect** (iamb) | assonance | synonyms: save and guard | I will rescue you and protect you evermore |
| 83 | **rescue** (trochee) / **defend** (iamb) | assonance | synonyms: save and shield | Rescue the dreamers and defend the dream |
| 84 | **strengthen** (trochee) / **defend** (iamb) | assonance | synonyms: fortify and guard | We strengthen every wall and defend the ones we love |
| 85 | **trekking** (trochee) / **stepping** (trochee) | assonance | synonyms: walking onward | Trekking through the hills and stepping toward the sun |
| 86 | **refuge** (trochee) / **rescue** (trochee) | assonance | cause/effect: rescue brings refuge | You came to my rescue and became my refuge |
| 87 | **wedding** (trochee) / **blessing** (trochee) | assonance | same scene: wedding vows | Our wedding day, a blessing from above |
| 88 | **festive** (trochee) / **presents** (trochee) | assonance | same scene: holiday gift exchange | Festive lights and presents by the tree |
| 89 | **necklace** (trochee) / **pendant** (trochee) | assonance | part/whole: pendant on necklace | A silver pendant on a golden necklace |
| 90 | **precious** (trochee) / **necklace** (trochee) | assonance | same scene: jewelry box treasures | A precious necklace that my mother wore |
| 91 | **meadow** (trochee) / **echo** (trochee) | assonance | same scene: open green valley | Hear the echo of our laughter in the meadow |
| 92 | **message** (trochee) / **sending** (trochee) | assonance | cause/effect: sending a message | I'm sending you a message full of love |
| 93 | **nexus** (trochee) / **connect** (iamb) | assonance | synonyms: link and connection | Two hearts connect at the nexus of the stars |
| 94 | **friendship** (trochee) / **endless** (trochee) | assonance | same theme: lasting bond | Our friendship is endless like the summer sky |
| 95 | **tempo** (trochee) / **techno** (trochee) | assonance | same domain: dance music | The techno beat picks up the tempo of the night |
| 96 | **fledgling** (trochee) / **nesting** (trochee) | assonance | same scene: young birds growing | A fledgling learns to fly from where the robins are nesting |
| 97 | **lemon** (trochee) / **lettuce** (trochee) | assonance | same scene: fresh garden salad | Squeeze a lemon on the lettuce from the garden |
| 98 | **veggie** (trochee) / **lettuce** (trochee) | assonance | part/whole: lettuce among veggies | Crisp lettuce leads the veggie basket home |
| 99 | **crescent** (trochee) / **heaven** (trochee) | assonance | same scene: night sky | A silver crescent glowing up in heaven |
| 100 | **fresco** (trochee) / **sketching** (trochee) | assonance | same domain: wall art making | Sketching on the wall until a fresco comes alive |

**Near-misses rejected (Short E)**

1. **presence / essence** — Both come from the Latin root esse (to be), so the rhyme repeats a shared morpheme.
2. **lemon / melon** — Melon is l-controlled because its stressed short E is closed by L, so it breaks the sound rules.
3. **heaven / eleven** — Eleven has three syllables, so it is neither an iamb nor a trochee.
4. **wedding / reading** — CMU only calls this a perfect rhyme because of the place-name pronunciation RED-ing, while the everyday word has a long E.
5. **necklace / reckless** — It is a perfect rhyme, but reckless is a negative word and the meaning link is too loose.

## Short I

/ɪ/ as in *wisdom, gifted* — CMU `IH` under primary stress.

| # | Pair | Rhyme type | Relationship | One-line example use |
|---|---|---|---|---|
| 1 | **living** (trochee) / **giving** (trochee) | perfect | cause/effect: giving enriches living | The secret of living is found in the giving |
| 2 | **kitten** (trochee) / **smitten** (trochee) | perfect | cause/effect: kitten leaves me smitten | One look at that kitten and I was smitten |
| 3 | **pretty** (trochee) / **witty** (trochee) | perfect | same domain: charming bright traits | She is pretty and witty and bright as the day |
| 4 | **drifting** (trochee) / **shifting** (trochee) | perfect | synonyms: slow gentle motion | Sands are shifting and the clouds are drifting |
| 5 | **ticking** (trochee) / **clicking** (trochee) | perfect | synonyms: small sharp sounds | The clock is ticking and the needles clicking |
| 6 | **kissing** (trochee) / **missing** (trochee) | perfect | antonyms: together versus apart | All day missing you, all night kissing you |
| 7 | **winning** (trochee) / **grinning** (trochee) | perfect | cause/effect: victory brings grins | We came home winning and we could not stop grinning |
| 8 | **lifted** (trochee) / **gifted** (trochee) | perfect | cause/effect: gift lifts heart | My heart was lifted by the love you gifted |
| 9 | **sitting** (trochee) / **knitting** (trochee) | perfect | same scene: cozy fireside evening | Grandma's sitting by the fire, knitting dreams in wool |
| 10 | **singing** (trochee) / **ringing** (trochee) | perfect | same scene: bells and choir | Church bells ringing while the choir is singing |
| 11 | **ringing** (trochee) / **bringing** (trochee) | perfect | cause/effect: bells bring cheer | Bells are ringing, bringing cheer to every street |
| 12 | **knitted** (trochee) / **fitted** (trochee) | perfect | cause/effect: handmade sweater fits | A sweater knitted just for me, perfectly fitted |
| 13 | **begin** (iamb) / **within** (iamb) | perfect | same domain: inner journey starts | Every great journey must begin within |
| 14 | **cricket** (trochee) / **wicket** (trochee) | perfect | part/whole: wicket in cricket | Summer cricket on the green, the ball flies past the wicket |
| 15 | **swimming** (trochee) / **skimming** (trochee) | perfect | same scene: summer lake surface | Swallows skimming where the children are swimming |
| 16 | **busy** (trochee) / **dizzy** (trochee) | perfect | cause/effect: busy day spins | Such a busy day it left me dizzy with delight |
| 17 | **city** (trochee) / **pretty** (trochee) | perfect | same scene: glowing city lights | The city looks so pretty in the rain |
| 18 | **drifted** (trochee) / **lifted** (trochee) | perfect | same scene: kite on breeze | The kite was lifted and it drifted out to sea |
| 19 | **thinking** (trochee) / **linking** (trochee) | perfect | cause/effect: thoughts connect ideas | Thinking of you, linking every star into a line |
| 20 | **pretty** (trochee) / **beauty** (trochee) | slant | synonyms: lovely to behold | Pretty as a picture, a beauty to behold |
| 21 | **mini** (trochee) / **tiny** (trochee) | slant | synonyms: very small size | A mini garden with a tiny rose |
| 22 | **busy** (trochee) / **lazy** (trochee) | slant | antonyms: bustle versus rest | Busy weekdays melting into lazy afternoons |
| 23 | **giddy** (trochee) / **steady** (trochee) | slant | antonyms: giddy versus steady | Giddy with love but steady as the sea |
| 24 | **predict** (iamb) / **expect** (iamb) | slant | synonyms: foresee what comes | No one could predict the joy we did not expect |
| 25 | **dismiss** (iamb) / **release** (iamb) | slant | synonyms: let things go | Dismiss your doubts and release them to the wind |
| 26 | **admit** (iamb) / **invite** (iamb) | slant | synonyms: welcome someone in | Open the door, admit the light, invite the morning in |
| 27 | **mixing** (trochee) / **fixing** (trochee) | perfect | same scene: kitchen cooking time | Mixing up the batter, fixing supper just for two |
| 28 | **sipping** (trochee) / **dipping** (trochee) | perfect | same scene: tea and biscuits | Sipping tea and dipping biscuits by the fire |
| 29 | **bridges** (trochee) / **ridges** (trochee) | perfect | same scene: mountain road trip | Over wooden bridges, up to sunny ridges |
| 30 | **lifting** (trochee) / **drifting** (trochee) | perfect | same scene: morning fog rising | Morning fog is lifting, drifting off the bay |
| 31 | **smitten** (trochee) / **written** (trochee) | perfect | cause/effect: love inspires letters | Every word was written by a heart so smitten |
| 32 | **swinging** (trochee) / **singing** (trochee) | perfect | same scene: playground summer joy | Swinging high and singing to the sky |
| 33 | **spinning** (trochee) / **grinning** (trochee) | perfect | same scene: carousel ride joy | Spinning on the carousel and grinning ear to ear |
| 34 | **skipping** (trochee) / **dipping** (trochee) | perfect | same scene: lakeside stone skipping | Skipping stones and dipping toes in the summer lake |
| 35 | **wishing** (trochee) / **fishing** (trochee) | perfect | same scene: lazy pond afternoon | Fishing by the pond and wishing on the breeze |
| 36 | **winning** (trochee) / **inning** (trochee) | perfect | same scene: final inning win | Bottom of the final inning and we are winning |
| 37 | **fishes** (trochee) / **dishes** (trochee) | perfect | same scene: seafood supper table | Silver fishes served on painted dishes |
| 38 | **printed** (trochee) / **tinted** (trochee) | perfect | same domain: ink and color | Printed petals on a page tinted rose |
| 39 | **gritty** (trochee) / **city** (trochee) | perfect | same scene: urban street life | Gritty city streets where dreams come alive |
| 40 | **enlist** (iamb) / **assist** (iamb) | perfect | cause/effect: enlisted friends assist | Enlist your friends and they will assist you |
| 41 | **given** (trochee) / **driven** (trochee) | perfect | cause/effect: gift sparks drive | Given a dream, I was driven to fly |
| 42 | **busy** (trochee) / **easy** (trochee) | slant | antonyms: hectic versus relaxed | Busy hands but an easy heart |
| 43 | **amid** (iamb) / **inside** (iamb) | slant | synonyms: in the midst | Amid the noise there's a quiet song inside |
| 44 | **insist** (iamb) / **request** (iamb) | slant | synonyms: ask from heart | I won't insist, it's just a soft request |
| 45 | **skipping** (trochee) / **leaping** (trochee) | slant | synonyms: joyful springing steps | Lambs are leaping and the children skipping |
| 46 | **winning** (trochee) / **gaining** (trochee) | slant | synonyms: getting ahead | Gaining ground and winning hearts along the way |
| 47 | **nifty** (trochee) / **crafty** (trochee) | slant | synonyms: clever and handy | Nifty little gadgets made by crafty hands |
| 48 | **gifted** (trochee) / **crafted** (trochee) | slant | cause/effect: talent shapes craft | Gifted hands have crafted every bead |
| 49 | **mission** (trochee) / **vision** (trochee) | slant | same domain: purpose and direction | Hold your vision close and live your mission |
| 50 | **mission** (trochee) / **passion** (trochee) | slant | same domain: driving inner purpose | Make your passion be your mission |
| 51 | **depict** (iamb) / **reflect** (iamb) | slant | synonyms: portray an image | Let my songs depict the love your eyes reflect |
| 52 | **tricky** (trochee) / **cheeky** (trochee) | slant | synonyms: playful little mischief | A cheeky grin and a tricky little wink |
| 53 | **listen** (trochee) / **lesson** (trochee) | slant | cause/effect: listening teaches lessons | If you listen, every day becomes a lesson |
| 54 | **given** (trochee) / **heaven** (trochee) | slant | same domain: blessings from above | Every blessing given is a gift from heaven |
| 55 | **living** (trochee) / **given** (trochee) | slant | same domain: life as gift | Every day of living is a gift we have been given |
| 56 | **kissing** (trochee) / **blessing** (trochee) | slant | same scene: wedding day joy | With a blessing from above, we're kissing at the altar |
| 57 | **wishes** (trochee) / **kisses** (trochee) | slant | same scene: birthday love notes | Sending birthday wishes wrapped in kisses |
| 58 | **begin** (iamb) / **again** (iamb) | slant | same domain: fresh new starts | Every sunrise lets us begin again |
| 59 | **within** (iamb) / **divine** (iamb) | slant | same domain: inner sacred spark | There's a spark divine within |
| 60 | **biscuit** (trochee) / **basket** (trochee) | slant | part/whole: biscuit in basket | A warm biscuit waiting in the basket |
| 61 | **windy** (trochee) / **sandy** (trochee) | slant | same scene: breezy beach day | Windy days along the sandy shore |
| 62 | **knitting** (trochee) / **chatting** (trochee) | slant | same scene: cozy knitting circle | Friends are chatting while the needles keep on knitting |
| 63 | **spinning** (trochee) / **swinging** (trochee) | slant | same scene: playground merry-go-round | Spinning round and swinging high |
| 64 | **fishing** (trochee) / **splashing** (trochee) | slant | same scene: summer lake fun | Fishing off the dock while the children are splashing |
| 65 | **fiction** (trochee) / **section** (trochee) | slant | part/whole: library fiction section | Lost all day in the fiction section |
| 66 | **wisdom** (trochee) / **insight** (trochee) | assonance | synonyms: deep understanding | Wisdom grows from every quiet insight |
| 67 | **vision** (trochee) / **insight** (trochee) | assonance | synonyms: clear inner seeing | A vision born of insight lights the way |
| 68 | **quickly** (trochee) / **swiftly** (trochee) | assonance | synonyms: at great speed | Quickly, swiftly, the river runs to the sea |
| 69 | **minute** (trochee) / **instant** (trochee) | assonance | synonyms: brief moment in time | In an instant, in a minute, love arrived |
| 70 | **smitten** (trochee) / **giddy** (trochee) | assonance | synonyms: lovestruck happy feelings | Smitten and giddy as a summer bride |
| 71 | **sipping** (trochee) / **drinking** (trochee) | assonance | synonyms: taking a drink | Sipping lemonade and drinking in the view |
| 72 | **whistling** (trochee) / **singing** (trochee) | assonance | synonyms: making happy tunes | Whistling while we work and singing all the way |
| 73 | **district** (trochee) / **city** (trochee) | assonance | part/whole: district of city | Every district of the city shining bright |
| 74 | **princess** (trochee) / **kingdom** (trochee) | assonance | part/whole: princess of kingdom | A princess dancing through her kingdom |
| 75 | **innings** (trochee) / **cricket** (trochee) | assonance | part/whole: innings in cricket | Long innings in the summer cricket sun |
| 76 | **kitchen** (trochee) / **dishes** (trochee) | assonance | same scene: kitchen sink chores | Singing in the kitchen while we wash the dishes |
| 77 | **chicken** (trochee) / **kitchen** (trochee) | assonance | same scene: farmhouse supper smells | Roast chicken warming up the kitchen |
| 78 | **chimney** (trochee) / **kitchen** (trochee) | assonance | same scene: cozy cottage hearth | Smoke from the chimney, bread in the kitchen |
| 79 | **picnic** (trochee) / **biscuits** (trochee) | assonance | same scene: picnic blanket treats | A picnic spread with honey biscuits |
| 80 | **crispy** (trochee) / **biscuits** (trochee) | assonance | same scene: fresh baked treats | Crispy biscuits cooling on the windowsill |
| 81 | **siblings** (trochee) / **kinship** (trochee) | assonance | same domain: family bonds | Siblings sharing kinship through the years |
| 82 | **kindred** (trochee) / **siblings** (trochee) | assonance | same domain: close family ties | Kindred hearts, like siblings, side by side |
| 83 | **gymnast** (trochee) / **fitness** (trochee) | assonance | same domain: athletic training | A gymnast's fitness shows in every turn |
| 84 | **knitting** (trochee) / **stitches** (trochee) | assonance | same domain: needlework craft | Knitting rows of tiny stitches by the light |
| 85 | **written** (trochee) / **fiction** (trochee) | assonance | same domain: storytelling craft | A fiction written by the candlelight |
| 86 | **ribbon** (trochee) / **linen** (trochee) | assonance | same scene: sewing basket | A ribbon tied on folded linen |
| 87 | **kitten** (trochee) / **ribbon** (trochee) | assonance | same scene: kitten chasing ribbon | A playful kitten chasing a satin ribbon |
| 88 | **mystic** (trochee) / **mythic** (trochee) | assonance | same domain: legend and magic | A mystic song from a mythic land |
| 89 | **vivid** (trochee) / **image** (trochee) | assonance | same domain: bright pictures | A vivid image of the summer sea |
| 90 | **misty** (trochee) / **windy** (trochee) | assonance | same scene: moorland weather | A misty morning on the windy hills |
| 91 | **misty** (trochee) / **midnight** (trochee) | assonance | same scene: moonlit misty night | A misty midnight and a silver moon |
| 92 | **fishing** (trochee) / **swimming** (trochee) | assonance | same scene: summer lake day | Fishing in the morning, swimming after noon |
| 93 | **thinking** (trochee) / **wisdom** (trochee) | assonance | cause/effect: thought builds wisdom | Quiet thinking slowly turns to wisdom |
| 94 | **thinking** (trochee) / **insight** (trochee) | assonance | cause/effect: thought brings insight | Quiet thinking brings a sudden insight |
| 95 | **prism** (trochee) / **vivid** (trochee) | assonance | cause/effect: prism makes colors | Through a prism vivid colors bloom |
| 96 | **springtime** (trochee) / **picnic** (trochee) | assonance | same scene: spring outing | A springtime picnic on the hill |
| 97 | **crimson** (trochee) / **ribbon** (trochee) | assonance | same scene: crimson ribbon gift | A crimson ribbon in your hair |
| 98 | **sprinting** (trochee) / **swimming** (trochee) | assonance | same domain: athletic races | Sprinting on the track and swimming in the pool |
| 99 | **pixie** (trochee) / **mystic** (trochee) | assonance | same domain: fairy magic | A pixie dancing in the mystic glade |
| 100 | **disco** (trochee) / **rhythm** (trochee) | assonance | same domain: dance floor beat | Disco lights and rhythm in our feet |

**Near-misses rejected (Short I)**

1. **shimmer / glimmer** — A lovely synonym pair, but both end in an r-controlled -er syllable (ER0), so neither word qualifies.
2. **twinkle / sprinkle** — A perfect rhyme for a starry scene, but the syllabic -le ending is l-controlled, so both fail the sound rules.
3. **admit / omit** — A perfect rhyme and a clean antonym, but both words share the Latin root -mit, so it is repetition rather than rhyme.
4. **wisdom / kingdom** — Most of the shared sound sits in the -dom suffix both words carry, so the link is barely from the stems.
5. **prison / risen** — A perfect rhyme, but prison is a negative word that clashes with the uplifting brief.

## Short O

/ɑ/, /ɔ/ as in *honest, softly* — CMU `AA, AO` under primary stress.

| # | Pair | Rhyme type | Relationship | One-line example use |
|---|---|---|---|---|
| 1 | **dotted** (trochee) / **spotted** (trochee) | perfect | synonyms: speckled with marks | Your dotted dress and spotted scarf go twirling down the lane |
| 2 | **chopping** (trochee) / **cropping** (trochee) | perfect | synonyms: cutting and trimming | Chopping wood and cropping hay beneath the harvest sun |
| 3 | **hopping** (trochee) / **stopping** (trochee) | perfect | antonyms: bouncing versus halting | Hopping down the garden path and never stopping |
| 4 | **hopping** (trochee) / **popping** (trochee) | perfect | synonyms: lively and buzzing | The dance floor's hopping and the music's popping |
| 5 | **hockey** (trochee) / **jockey** (trochee) | perfect | same domain: sporting athletes | From the hockey rink to the jockey's winning ride |
| 6 | **awesome** (trochee) / **blossom** (trochee) | perfect | same scene: wondrous spring bloom | What an awesome blossom opens on the cherry tree |
| 7 | **popping** (trochee) / **topping** (trochee) | perfect | same scene: buttered popcorn treat | Hear the kernels popping, pour the butter topping |
| 8 | **tonic** (trochee) / **sonic** (trochee) | perfect | same domain: musical sound | Start on the tonic note and ride the sonic wave |
| 9 | **rocking** (trochee) / **stocking** (trochee) | perfect | same scene: Christmas morning cheer | Rocking by the fireside with a stocking full of dreams |
| 10 | **pauses** (trochee) / **clauses** (trochee) | perfect | part/whole: rhythm of sentences | Love lives in the pauses between the clauses |
| 11 | **strongest** (trochee) / **longest** (trochee) | perfect | cause/effect: strength brings endurance | The strongest love is the one that lasts the longest |
| 12 | **shopping** (trochee) / **dropping** (trochee) | perfect | cause/effect: shop till you drop | We'll go shopping till we're dropping, laughing all the way |
| 13 | **broaden** (trochee) / **widen** (trochee) | slant | synonyms: making something wider | Broaden your horizons, let your circle widen |
| 14 | **broadly** (trochee) / **widely** (trochee) | slant | synonyms: across a wide range | Smile broadly, roam widely, the world is yours today |
| 15 | **fondly** (trochee) / **kindly** (trochee) | slant | synonyms: with warm affection | Remember me fondly and treat the stranger kindly |
| 16 | **fondness** (trochee) / **kindness** (trochee) | slant | synonyms: warm tender affection | Your fondness and your kindness are the light that leads me home |
| 17 | **spotted** (trochee) / **sighted** (trochee) | slant | synonyms: caught sight of | We spotted the first star as the sailors sighted land |
| 18 | **hopping** (trochee) / **skipping** (trochee) | slant | synonyms: light bouncing steps | Hopping over puddles, skipping down the lane |
| 19 | **logic** (trochee) / **magic** (trochee) | slant | antonyms: reason versus wonder | Forget the logic, darling, love is magic |
| 20 | **pocket** (trochee) / **jacket** (trochee) | slant | part/whole: pocket of jacket | A love note tucked in the pocket of your jacket |
| 21 | **dotted** (trochee) / **plotted** (trochee) | perfect | same scene: mapping a route | We plotted our course along a dotted line |
| 22 | **shopping** (trochee) / **swapping** (trochee) | perfect | same domain: trading goods | Shopping at the market, swapping stories with our friends |
| 23 | **crossing** (trochee) / **tossing** (trochee) | perfect | same scene: boat on waves | Crossing the bay with the waves gently tossing |
| 24 | **knocking** (trochee) / **locking** (trochee) | perfect | same scene: opening the door | Love came knocking, so I quit locking my heart away |
| 25 | **abroad** (iamb) / **applaud** (iamb) | perfect | same scene: acclaimed tour abroad | We sing abroad and the whole world stands to applaud |
| 26 | **fondly** (trochee) / **friendly** (trochee) | slant | synonyms: warm and welcoming | She waves so fondly, every face is friendly |
| 27 | **spotted** (trochee) / **noted** (trochee) | slant | synonyms: noticed and observed | I spotted your smile and noted every spark |
| 28 | **spotting** (trochee) / **sighting** (trochee) | slant | synonyms: catching first glimpse | Spotting the first robin is the sighting of the spring |
| 29 | **beyond** (iamb) / **transcend** (iamb) | slant | synonyms: rising past limits | Look beyond the clouds and let your heart transcend |
| 30 | **glossy** (trochee) / **classy** (trochee) | slant | synonyms: sleek polished style | Glossy shoes and a classy little tune |
| 31 | **glossy** (trochee) / **messy** (trochee) | slant | antonyms: polished versus untidy | From glossy curls to messy hair, I love you either way |
| 32 | **softly** (trochee) / **safely** (trochee) | slant | synonyms: gentle and protective | Hold me softly, keep me safely in your arms |
| 33 | **wanted** (trochee) / **granted** (trochee) | slant | cause/effect: wish comes true | Every star I wanted, every wish was granted |
| 34 | **honest** (trochee) / **promised** (trochee) | slant | cause/effect: truth keeps promises | An honest heart gives all it promised |
| 35 | **bonding** (trochee) / **blending** (trochee) | slant | synonyms: coming together as one | Hearts are bonding, voices blending into one |
| 36 | **along** (iamb) / **among** (iamb) | slant | synonyms: together with others | Sing along among the friends who love you |
| 37 | **softly** (trochee) / **swiftly** (trochee) | slant | antonyms: gentle versus quick | The river whispers softly and the swallows swiftly fly |
| 38 | **adopt** (iamb) / **accept** (iamb) | slant | synonyms: welcoming someone in | Open arms adopt you, open hearts accept you |
| 39 | **crossing** (trochee) / **passing** (trochee) | slant | synonyms: traveling across or past | Crossing every bridge and passing every mile |
| 40 | **rocking** (trochee) / **shaking** (trochee) | slant | synonyms: dancing body movement | The whole room's rocking and the floor is shaking |
| 41 | **cotton** (trochee) / **satin** (trochee) | slant | same domain: soft fabrics | Cotton sheets and satin ribbons in the summer breeze |
| 42 | **frosty** (trochee) / **misty** (trochee) | slant | same scene: cold winter morning | A frosty morning, misty fields of white |
| 43 | **frosted** (trochee) / **toasted** (trochee) | slant | same scene: bakery breakfast table | Frosted buns and toasted bread to start the day |
| 44 | **frosting** (trochee) / **tasting** (trochee) | slant | same scene: baking a cake | Sneaking frosting, tasting sugar off the spoon |
| 45 | **cotton** (trochee) / **button** (trochee) | slant | part/whole: button on shirt | Sew a button on my cotton Sunday shirt |
| 46 | **donkey** (trochee) / **monkey** (trochee) | slant | same domain: barnyard and zoo | A donkey and a monkey dancing at the fair |
| 47 | **comic** (trochee) / **mimic** (trochee) | slant | same domain: comedy performers | The comic and the mimic keep the crowd in stitches |
| 48 | **pocket** (trochee) / **ticket** (trochee) | slant | same scene: ready to travel | A ticket in my pocket and the open road ahead |
| 49 | **washing** (trochee) / **splashing** (trochee) | slant | same scene: bath time fun | Washing in the creek and splashing in the sun |
| 50 | **rocky** (trochee) / **foggy** (trochee) | slant | same scene: misty mountain trail | Foggy mornings on the rocky mountain trail |
| 51 | **chopping** (trochee) / **prepping** (trochee) | slant | same scene: kitchen supper prep | Chopping herbs and prepping supper while we sing |
| 52 | **topping** (trochee) / **dipping** (trochee) | slant | same scene: dessert bar | Strawberries for dipping and whipped cream for topping |
| 53 | **longing** (trochee) / **singing** (trochee) | slant | same scene: love song | My longing turns to singing every time you call |
| 54 | **applause** (iamb) / **amaze** (iamb) | slant | cause/effect: wonder earns applause | You amaze them all and they rise in applause |
| 55 | **applaud** (iamb) / **parade** (iamb) | slant | same scene: cheering street parade | Wave your flags and applaud as the bright parade goes by |
| 56 | **upon** (iamb) / **began** (iamb) | slant | same scene: story opening | Once upon a time our story began |
| 57 | **softly** (trochee) / **briefly** (trochee) | slant | same scene: tender passing kiss | Kiss me softly, kiss me briefly, then kiss me once again |
| 58 | **beyond** (iamb) / **ascend** (iamb) | slant | same scene: rising skyward | Ascend the hill and see the stars beyond |
| 59 | **beyond** (iamb) / **extend** (iamb) | slant | same scene: reaching past horizons | Extend your hand and reach for the stars beyond |
| 60 | **comet** (trochee) / **summit** (trochee) | slant | same scene: mountain night sky | A comet blazing over the snowy summit |
| 61 | **shopping** (trochee) / **shipping** (trochee) | slant | same domain: online orders | Shopping from the sofa, free shipping to my door |
| 62 | **hottest** (trochee) / **brightest** (trochee) | slant | same scene: summer midday sun | The hottest day of summer and the brightest sun |
| 63 | **tossing** (trochee) / **passing** (trochee) | slant | same scene: playing catch | Tossing the ball and passing it back across the park |
| 64 | **pausing** (trochee) / **crossing** (trochee) | slant | same scene: careful street crossing | Pausing at the corner, then crossing hand in hand |
| 65 | **pausing** (trochee) / **gazing** (trochee) | slant | same scene: hilltop view | Pausing on the hilltop, gazing at the sea |
| 66 | **plotting** (trochee) / **writing** (trochee) | slant | same domain: storytelling craft | Plotting out the chapters, writing down our dreams |
| 67 | **popping** (trochee) / **clapping** (trochee) | slant | same scene: celebration party | Corks are popping, hands are clapping, happy new year |
| 68 | **cotton** (trochee) / **kitten** (trochee) | slant | same domain: soft fluffy things | Soft as cotton, sleepy as a kitten |
| 69 | **robin** (trochee) / **cabin** (trochee) | slant | same scene: woodland cabin morning | A robin sings outside our little cabin door |
| 70 | **bonding** (trochee) / **spending** (trochee) | slant | same scene: quality time together | Bonding over pancakes, spending Sunday slow |
| 71 | **across** (iamb) / **embrace** (iamb) | slant | same scene: joyful reunion | Run across the room and fall into my embrace |
| 72 | **salon** (iamb) / **champagne** (iamb) | slant | same scene: elegant evening soiree | Champagne laughter in the candlelit salon |
| 73 | **atop** (iamb) / **bottom** (trochee) | assonance | antonyms: top versus bottom | From the bottom of the hill to atop the highest peak |
| 74 | **comic** (trochee) / **drama** (trochee) | assonance | antonyms: comedy versus drama | Half the night was comic, half was drama on the stage |
| 75 | **honest** (trochee) / **modest** (trochee) | assonance | same domain: humble virtues | An honest word, a modest heart, that's all I need |
| 76 | **promise** (trochee) / **constant** (trochee) | assonance | same domain: faithful devotion | A constant heart will always keep its promise |
| 77 | **mama** (trochee) / **papa** (trochee) | assonance | same domain: loving parents | Mama hums and papa sings us both to sleep |
| 78 | **coffee** (trochee) / **latte** (trochee) | assonance | same domain: morning cafe drinks | Black coffee for you, a creamy latte for me |
| 79 | **coffee** (trochee) / **office** (trochee) | assonance | same scene: office break room | Fresh coffee brewing in the office every morning |
| 80 | **awesome** (trochee) / **applause** (iamb) | assonance | cause/effect: great show earns applause | What an awesome show, the whole room rings with applause |
| 81 | **watching** (trochee) / **spotting** (trochee) | assonance | synonyms: looking and observing | Watching for the fireflies and spotting every glow |
| 82 | **fondness** (trochee) / **bonding** (trochee) | assonance | cause/effect: affection builds closeness | Our fondness keeps on bonding us together |
| 83 | **autumn** (trochee) / **august** (trochee) | assonance | same domain: late summer months | August slips away and autumn paints the trees |
| 84 | **blossom** (trochee) / **robin** (trochee) | assonance | same scene: spring garden | A robin sings where every blossom grows |
| 85 | **bravo** (trochee) / **drama** (trochee) | assonance | same scene: stage curtain call | Bravo for the drama, take another bow tonight |
| 86 | **comet** (trochee) / **rocket** (trochee) | assonance | same scene: night sky | Ride a rocket, chase a comet through the night |
| 87 | **frosting** (trochee) / **glossy** (trochee) | assonance | same scene: shiny iced cake | Glossy pink frosting on a birthday cake for you |
| 88 | **autumn** (trochee) / **frosty** (trochee) | assonance | same scene: crisp cold season | Autumn leaves on frosty mornings crunch beneath our feet |
| 89 | **coffee** (trochee) / **autumn** (trochee) | assonance | same scene: cozy fall morning | Warm coffee on a golden autumn day |
| 90 | **blossom** (trochee) / **poppy** (trochee) | assonance | same domain: spring flowers | A poppy blooms beside the apple blossom |
| 91 | **hockey** (trochee) / **hobby** (trochee) | assonance | same domain: weekend pastimes | Hockey on the frozen pond is my favorite winter hobby |
| 92 | **bravo** (trochee) / **spotlight** (trochee) | assonance | same scene: curtain call ovation | Bravo, the spotlight finds you as the curtain falls |
| 93 | **taco** (trochee) / **nacho** (trochee) | assonance | same domain: Mexican food | A taco night with a nacho plate to share |
| 94 | **cottage** (trochee) / **lodging** (trochee) | assonance | synonyms: places to stay | A cozy cottage gives us lodging for the night |
| 95 | **comet** (trochee) / **cosmos** (trochee) | assonance | same domain: outer space | A comet streaking through the cosmos just for you |
| 96 | **cosmic** (trochee) / **rocket** (trochee) | assonance | same domain: space travel | Board the rocket for a cosmic ride tonight |
| 97 | **octave** (trochee) / **tonic** (trochee) | assonance | same domain: musical scale | Climb an octave, then fall back home to the tonic |
| 98 | **saga** (trochee) / **drama** (trochee) | assonance | same domain: epic storytelling | Our love's a saga full of drama and delight |
| 99 | **cottage** (trochee) / **condo** (trochee) | assonance | same domain: holiday homes | Trade the city condo for a cottage by the sea |
| 100 | **condo** (trochee) / **lobby** (trochee) | assonance | part/whole: lobby of building | Meet me in the lobby of your condo after dark |

**Near-misses rejected (Short O)**

1. **walking / talking** — A perfect rhyme for strolling side by side, but the silent-L spelling (alk) now counts as l-controlled, so neither word qualifies.
2. **along / belong** — A perfect rhyme about being together, but both words visibly share the morpheme "long", so it reads as repetition, not rhyme.
3. **collage / montage** — A perfect rhyme for near-synonyms, but the whole sound link comes from the shared French suffix -age rather than the stems.
4. **sonic / harmonic** — A tight musical link, but harmonic has three syllables (and an r-controlled first syllable), so it fails the meter rule.
5. **wander / ponder** — A perfect rhyme for dreamy, musing thought, but both words end in an r-controlled -er syllable.

## Short U

/ʌ/ as in *sunny, lovely* — CMU `AH` under primary stress.

| # | Pair | Rhyme type | Relationship | One-line example use |
|---|---|---|---|---|
| 1 | **sunny** (trochee) / **funny** (trochee) | perfect | synonyms: cheerful bright moods | You turn a sunny morning funny with that laugh of yours |
| 2 | **yummy** (trochee) / **tummy** (trochee) | perfect | cause/effect: treats fill tummy | Something yummy warms my tummy on a winter night |
| 3 | **fluffy** (trochee) / **puffy** (trochee) | perfect | synonyms: soft swollen clouds | Fluffy clouds go drifting by so puffy and so white |
| 4 | **rubbing** (trochee) / **scrubbing** (trochee) | perfect | synonyms: cleaning by hand | Rubbing and scrubbing till the windows shine like gold |
| 5 | **conduct** (iamb) / **instruct** (iamb) | perfect | synonyms: guide and teach | Let love conduct the music and instruct my heart to sing |
| 6 | **humming** (trochee) / **drumming** (trochee) | perfect | same scene: making happy music | You're humming in the kitchen while I'm drumming on the door |
| 7 | **honey** (trochee) / **bunny** (trochee) | perfect | synonyms: sweet pet names | Come here, honey, come here, bunny, let me hold you tight |
| 8 | **study** (trochee) / **buddy** (trochee) | perfect | same scene: learning together partners | Every study night is better with my buddy by my side |
| 9 | **cousins** (trochee) / **dozens** (trochee) | perfect | same scene: big family reunion | Dozens of cousins dancing in the summer grass |
| 10 | **jumping** (trochee) / **thumping** (trochee) | perfect | cause/effect: leaping makes thumping | Jumping on the trampoline, my heart is thumping loud |
| 11 | **touching** (trochee) / **clutching** (trochee) | perfect | synonyms: holding with hands | Touching your hand and clutching it close to my heart |
| 12 | **rushing** (trochee) / **blushing** (trochee) | perfect | cause/effect: rushing blood, blush | Warmth is rushing to my cheeks, I'm blushing at your name |
| 13 | **dusty** (trochee) / **rusty** (trochee) | perfect | synonyms: old weathered things | Dusty boots and rusty keys still lead me home to you |
| 14 | **trusty** (trochee) / **rusty** (trochee) | perfect | same scene: old reliable truck | My trusty rusty pickup rolls along the coast |
| 15 | **dusty** (trochee) / **trusty** (trochee) | perfect | same scene: cowboy trail ride | Riding down the dusty trail upon my trusty horse |
| 16 | **jumping** (trochee) / **bumping** (trochee) | perfect | same scene: lively dance floor | We're jumping and bumping to the beat all night |
| 17 | **monkey** (trochee) / **funky** (trochee) | perfect | same scene: playful dancing fun | Dance like a funky monkey underneath the moon |
| 18 | **chunky** (trochee) / **funky** (trochee) | perfect | same domain: bold groovy style | Chunky boots and funky shoes are dancing down the street |
| 19 | **loving** (trochee) / **giving** (trochee) | slant | synonyms: generous warm heart | A loving heart is always giving more |
| 20 | **lovely** (trochee) / **lively** (trochee) | slant | synonyms: bright and charming | A lovely, lively morning full of song |
| 21 | **trusted** (trochee) / **tested** (trochee) | slant | synonyms: proven and reliable | A friendship tested, trusted, and true |
| 22 | **sunny** (trochee) / **shiny** (trochee) | slant | synonyms: bright and gleaming | A sunny sky and shiny dreams ahead |
| 23 | **fuzzy** (trochee) / **cozy** (trochee) | slant | synonyms: soft warm comfort | Fuzzy socks and cozy nights beside the fire |
| 24 | **rushing** (trochee) / **dashing** (trochee) | slant | synonyms: hurrying along quickly | Rushing through the station, dashing for the train to you |
| 25 | **rugged** (trochee) / **jagged** (trochee) | slant | synonyms: rough mountain terrain | Rugged cliffs and jagged peaks are calling me |
| 26 | **yummy** (trochee) / **creamy** (trochee) | slant | synonyms: rich tasty dessert | Yummy, creamy ice cream melting in the sun |
| 27 | **stunning** (trochee) / **shining** (trochee) | slant | synonyms: brilliant radiant beauty | You look stunning, shining like the morning star |
| 28 | **fuzzy** (trochee) / **hazy** (trochee) | slant | synonyms: blurry soft focus | Fuzzy, hazy summer afternoons drift slowly by |
| 29 | **brushing** (trochee) / **washing** (trochee) | slant | synonyms: daily cleaning chores | Brushing my hair and washing my face in the morning light |
| 30 | **puppy** (trochee) / **happy** (trochee) | slant | same scene: joyful wagging dog | A happy puppy chasing butterflies |
| 31 | **study** (trochee) / **ready** (trochee) | slant | cause/effect: study makes ready | I study every night so I'll be ready for the day |
| 32 | **running** (trochee) / **winning** (trochee) | slant | cause/effect: running brings winning | Keep on running and you'll keep on winning |
| 33 | **among** (iamb) / **belong** (iamb) | slant | same scene: belonging together | Among the stars is where we both belong |
| 34 | **rustic** (trochee) / **plastic** (trochee) | slant | antonyms: natural versus synthetic | Rustic wood, not plastic, in our cabin home |
| 35 | **touching** (trochee) / **reaching** (trochee) | slant | same scene: hands stretching skyward | Reaching for the stars and touching the sky |
| 36 | **buddy** (trochee) / **teddy** (trochee) | slant | same scene: childhood cuddly companion | My teddy was my buddy every night |
| 37 | **humming** (trochee) / **blooming** (trochee) | slant | same scene: spring garden bees | Bees are humming and the roses blooming in the yard |
| 38 | **begun** (iamb) / **again** (iamb) | slant | same scene: starting over fresh | A brand new day has begun again |
| 39 | **loving** (trochee) / **living** (trochee) | slant | same scene: love-filled life | Loving you is living free |
| 40 | **trusting** (trochee) / **lasting** (trochee) | slant | cause/effect: trust builds lasting love | A trusting heart will build a lasting love |
| 41 | **summit** (trochee) / **limit** (trochee) | slant | same domain: highest point reached | Climb up to the summit, the sky is the limit |
| 42 | **nutty** (trochee) / **witty** (trochee) | slant | synonyms: playful silly humor | Your nutty jokes and witty lines keep me smiling |
| 43 | **bunny** (trochee) / **pony** (trochee) | slant | same scene: children's pet farm | A bunny and a pony playing in the meadow |
| 44 | **bunny** (trochee) / **tiny** (trochee) | slant | same scene: small soft creature | A tiny bunny hopping through the clover |
| 45 | **honey** (trochee) / **yummy** (trochee) | slant | same scene: sweet sticky treats | Honey on my toast tastes yummy every time |
| 46 | **muffin** (trochee) / **oven** (trochee) | slant | same scene: morning kitchen baking | A muffin rising golden in the oven |
| 47 | **button** (trochee) / **kitten** (trochee) | slant | same scene: cute little things | Cute as a button, soft as a kitten |
| 48 | **touching** (trochee) / **teaching** (trochee) | slant | same domain: inspiring young hearts | Teaching every child and touching every heart |
| 49 | **dusty** (trochee) / **misty** (trochee) | slant | same scene: hazy country morning | Dusty roads and misty hills at dawn |
| 50 | **rusty** (trochee) / **frosty** (trochee) | slant | same scene: old winter gate | The rusty gate is frosty in the morning |
| 51 | **lunches** (trochee) / **benches** (trochee) | slant | same scene: park picnic break | Eating lunches on the benches by the lake |
| 52 | **budding** (trochee) / **seeding** (trochee) | slant | cause/effect: seeds bring buds | Seeding in the spring brings budding trees |
| 53 | **buzzing** (trochee) / **grazing** (trochee) | slant | same scene: summer meadow life | Bees are buzzing, cattle grazing in the sun |
| 54 | **jumping** (trochee) / **camping** (trochee) | slant | same scene: summer outdoor fun | Camping by the lake and jumping in at noon |
| 55 | **coming** (trochee) / **running** (trochee) | slant | same scene: hurrying home happily | Hear me coming running home to you |
| 56 | **rushing** (trochee) / **splashing** (trochee) | slant | same scene: river rapids flowing | Rushing water splashing on the stones |
| 57 | **cousins** (trochee) / **seasons** (trochee) | slant | same scene: holiday family gatherings | Holiday seasons spent with all my cousins |
| 58 | **puppy** (trochee) / **sleepy** (trochee) | slant | same scene: napping little pet | A sleepy puppy curled up on my lap |
| 59 | **buddy** (trochee) / **steady** (trochee) | slant | same scene: loyal reliable friend | My steady buddy through it all |
| 60 | **sunday** (trochee) / **sandy** (trochee) | slant | same scene: beach weekend fun | Sunday morning on the sandy shore |
| 61 | **nutty** (trochee) / **fruity** (trochee) | slant | same domain: trail mix flavors | Nutty, fruity granola in the morning |
| 62 | **puppy** (trochee) / **floppy** (trochee) | slant | part/whole: floppy puppy ears | A puppy with floppy ears is waiting at the door |
| 63 | **oven** (trochee) / **heaven** (trochee) | slant | same scene: heavenly fresh baking | Bread straight from the oven smells like heaven |
| 64 | **stuffing** (trochee) / **oven** (trochee) | slant | same scene: holiday roast dinner | The stuffing in the oven fills the house with cheer |
| 65 | **country** (trochee) / **pantry** (trochee) | slant | same scene: farmhouse kitchen shelves | A country pantry full of jam and bread |
| 66 | **hugging** (trochee) / **cuddling** (trochee) | assonance | synonyms: warm close embrace | Hugging and cuddling underneath the stars |
| 67 | **fluffy** (trochee) / **cuddly** (trochee) | assonance | synonyms: soft and huggable | A fluffy, cuddly kitten curled up in my arms |
| 68 | **lovely** (trochee) / **stunning** (trochee) | assonance | synonyms: truly beautiful sight | You look lovely, you look stunning in the light |
| 69 | **upbeat** (trochee) / **funny** (trochee) | assonance | synonyms: cheerful good humor | Your upbeat songs and funny stories light the room |
| 70 | **sunny** (trochee) / **upbeat** (trochee) | assonance | synonyms: cheerful bright outlook | A sunny smile and an upbeat heart |
| 71 | **money** (trochee) / **funding** (trochee) | assonance | synonyms: financial support | The money and the funding helped our garden grow |
| 72 | **buzzing** (trochee) / **humming** (trochee) | assonance | synonyms: busy bee sounds | Buzzing and humming, the bees are making honey |
| 73 | **country** (trochee) / **rustic** (trochee) | assonance | synonyms: rural simple charm | A rustic cabin in the country hills |
| 74 | **rugged** (trochee) / **robust** (iamb) | assonance | synonyms: strong and sturdy | Rugged hands and a robust heart |
| 75 | **nutmeg** (trochee) / **pumpkin** (trochee) | assonance | same scene: autumn pie spices | Nutmeg dusted on the pumpkin pie |
| 76 | **onion** (trochee) / **mushroom** (trochee) | assonance | same scene: savory kitchen cooking | An onion and a mushroom sizzling in the pan |
| 77 | **drumming** (trochee) / **trumpet** (trochee) | assonance | same domain: marching band music | Drumming and a trumpet leading the parade |
| 78 | **trumpet** (trochee) / **summon** (trochee) | assonance | cause/effect: trumpet call gathers | The trumpet sounds to summon us to dance |
| 79 | **loving** (trochee) / **hugging** (trochee) | assonance | same scene: warm affection shared | Loving and hugging all the way home |
| 80 | **money** (trochee) / **budget** (trochee) | assonance | same domain: careful spending plans | We saved our money on a little budget |
| 81 | **hundred** (trochee) / **dozen** (trochee) | assonance | same domain: counting big numbers | A dozen roses, then a hundred more |
| 82 | **lunchtime** (trochee) / **hungry** (trochee) | assonance | cause/effect: noon brings appetite | By lunchtime I am hungry for a picnic in the sun |
| 83 | **honey** (trochee) / **buzzing** (trochee) | assonance | same scene: busy beehive day | Honey dripping while the hive is buzzing |
| 84 | **discuss** (iamb) / **study** (trochee) | assonance | same domain: learning together | Let's discuss the stars we study every night |
| 85 | **husband** (trochee) / **trusted** (trochee) | assonance | same scene: faithful married partner | My husband is my trusted friend for life |
| 86 | **comfy** (trochee) / **cuddly** (trochee) | assonance | synonyms: cozy and soft | A comfy chair, a cuddly blanket |
| 87 | **stuffing** (trochee) / **pumpkin** (trochee) | assonance | same scene: harvest holiday feast | Stuffing on the table, pumpkin pie to share |
| 88 | **dozen** (trochee) / **muffins** (trochee) | assonance | same scene: bakery box treats | A dozen muffins warm for breakfast |
| 89 | **compass** (trochee) / **summit** (trochee) | assonance | same scene: mountain hiking trip | Follow the compass to the summit |
| 90 | **tundra** (trochee) / **husky** (trochee) | assonance | same scene: arctic sled run | A husky racing on the snowy tundra |
| 91 | **upright** (trochee) / **justice** (trochee) | assonance | same domain: moral integrity | An upright heart will always stand for justice |
| 92 | **clubhouse** (trochee) / **buddies** (trochee) | assonance | same scene: friends' secret hangout | Meet my buddies at the clubhouse after school |
| 93 | **touchdown** (trochee) / **rugby** (trochee) | assonance | same domain: ball sports | A touchdown in the rugby match |
| 94 | **mustang** (trochee) / **running** (trochee) | assonance | same scene: wild horse galloping | A mustang running free across the plain |
| 95 | **above** (iamb) / **summit** (trochee) | assonance | same domain: lofty mountain heights | The summit rising high above the clouds |
| 96 | **above** (iamb) / **sunlight** (trochee) | assonance | same scene: bright sky overhead | Golden sunlight shining from above |
| 97 | **wondrous** (trochee) / **stunning** (trochee) | assonance | synonyms: amazing and beautiful | A wondrous, stunning view from here |
| 98 | **among** (iamb) / **cousins** (trochee) | assonance | same scene: family gathering together | Laughing among my cousins at the fair |
| 99 | **among** (iamb) / **buddies** (trochee) | assonance | same scene: friends gathered together | Laughing among my buddies by the fire |
| 100 | **dusting** (trochee) / **scrubbing** (trochee) | assonance | same scene: spring cleaning day | Dusting shelves and scrubbing floors on a bright spring day |

**Near-misses rejected (Short U)**

1. **sunday / monday** — A perfect rhyme of two weekdays, but both words end in the shared morpheme "day", so the match is repetition, not rhyme.
2. **sunlight / moonlight** — A strong slant with a clear antonym link, but the shared morpheme "light" supplies the whole sound match.
3. **something / nothing** — A vivid antonym pair, but both are built on the same root "thing", and CMU gives only assonance.
4. **husband / hubby** — The meaning is a tight synonym, but hubby is just a clipped form of husband, so they share a root.
5. **mummy / tummy** — A perfect rhyme in a mother-and-child scene, but "mummy" also means an embalmed corpse, which brings in a death image the brief rules out.
