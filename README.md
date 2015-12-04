dnsmonitor.py - სკრიპტი ადარებს ერთი "სანდო" დნს რესოლვერის პასუხებს, სხვა მითითებულ დნს სერვერების პასუხებთან. თუ რომელიმე მათგანი იყო განსხვავებული, შედეგებს აგზავნის მითითებულ მეილ მისამართზე. ამ მეთოდით შესაძლოა მონიტორინგი გაუკეთდეს ცნობილ პაბლიქ დნს რესოლვერებს სპუფინგზე ან ცენზურა/თაღლითობაზე.

სკრიპტს მუშაობისთვის ჭირდება შემდეგი რამეები: 
 1. "სანდო" დნს სერვერის მისამართი, ამჯერად მითითებულია 8.8.8.8
 2. servers.txt ფაილი იგივე დირექტორიაში, სადაც ჩამოწერილი იქნება სამონიტორინგო დნს სერვერების მისამართები.
 3. domains.txt ფაილი იგივე დირექტორიაში, სადაც ჩამოწერილი იქნება ის დომეინ მისამართები, რომლითაც შემოწმდება სერვერები.
 4. მუშა მეილ სერვერი და აქტიური ანგარიში. შეგიძლიათ გამოიყენოთ gmail ან სხვა მეილ სერვერები. თუმცა სკრიპტი შედეგებს dnsmonitor.log ფაილშიც ჩაწერს და მეილ სერვერი აუცილებელი არ არის.

პ.ს. ეს იდეა მომივიდა იმის მერე, რაც ბოლო 3 წლის განმავლობაში ჩვენს ქვეყანაში არსებული ორი დიდი პროვაიდერის დნს სერვერებზე მოხდა სპუფინგ შეტევა და ხალხი მისამართდებოდა სხვა გვერდებზე.

dnsmonitor.py - script which compares answers from one "trusted" DNS resolver server and from other servers from list. If one or more servers from list will answer differently, then script sends email alert. With this script, you can monitor servers for spoofing.

script needs several things to work: 
 1. "trusted" dns resolver address, by default it is 8.8.8.8
 2. servers.txt file with list of dns resolvers for monitoring
 3. domains.txt file with list of domains by which script will monitor servers.
 4. mail server and account on it. you can use gmail or other public servers. But it's optional, because script will log any alerts in dnsmonitor.log file.
