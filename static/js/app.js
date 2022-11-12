//How to run Flask application
//flask --app main.py --debug run

//for the logout button

/* console.log("Hello");

logoutButton = document.getElementById("logoutButton");
loggedOurAlertDiv = document.getElementById("loggedOutAlert");

console.log(logoutButton);

logoutButton.addEventListener("click", () => {
  console.log("fag");
  loggedOurAlertDiv.classList.remove("d-none");
}); */

const formatter = new Intl.NumberFormat("en-US", {
  style: "currency",
  currency: "USD",

  // These options are needed to round to whole numbers if that's what you want.
  //minimumFractionDigits: 0, // (this suffices for whole numbers, but will print 2500.10 as $2,500.1)
  //maximumFractionDigits: 0, // (causes 2500.99 to be printed as $2,501)
});

try {
  investmentSum = document.getElementById("investmentSum");
  console.log(investmentSum.innerText);
  investmentSum.innerText = formatter.format(investmentSum.innerText);
} catch (error) {
  console.log(error);
}

try {
  inputPrice = document.getElementsByClassName("inputPrice");
  console.log(inputPrice);

  formPrice = document.getElementsByClassName("formPrice");

  console.log(formPrice[0]);

  for (let i = 0; i < formPrice.length; i++) {
    formPrice[i]["innerText"] = formatter.format(formPrice[i]["innerText"]);
  }

  for (let i = 0; i < inputPrice.length; i++) {
    inputPrice[i].value = formPrice[i]["innerText"];
  }
} catch (error) {
  console.log(error);
}

try {
  cash = document.getElementById("cashOnHandFormatter");
  notificationMoney = document.getElementById("moreMoneyNotice");
  formPrice = document.getElementsByClassName("formPrice");

  console.log(parseInt(cash.innerText));
  console.log(Math.sign(parseInt(cash.innerText)));

  if (Math.sign(parseInt(cash.innerText)) == -1) {
    notificationMoney.classList.add("alert");
    notificationMoney.classList.add("alert-danger");
  } else {
    //notificationMoney.classList.remove("alert");
    notificationMoney.style.display = "none";
  }

  cash["innerText"] = formatter.format(cash["innerText"]);
} catch (error) {
  console.log(error);
}

dollars = document.getElementsByClassName("usd");

for (var i = 0; i < dollars.length; i++) {
  dollars[i]["innerText"] = formatter.format(dollars[i]["outerText"]);
}

//console.log(deleteButton[0].parentNode.parentNode.remove);
let savingsTemp = localStorage.getItem("savings");
let needsTemp = localStorage.getItem("needs");
let wantsTemp = localStorage.getItem("wants");

if ((savingsTemp == "NaN") | (needsTemp == "NaN") | (wantsTemp == "NaN")) {
  localStorage.setItem("savings", 60);
  localStorage.setItem("needs", 60);
  localStorage.setItem("wants", 60);
  localStorage.setItem("total", 180);
}

if ((savingsTemp == 0) & (needsTemp == 0) & (wantsTemp == 0)) {
  localStorage.setItem("savings", 60);
  localStorage.setItem("needs", 60);
  localStorage.setItem("wants", 60);
  localStorage.setItem("total", 180);
}

console.log(localStorage.getItem("needs"));
console.log(localStorage.getItem("wants"));
console.log(localStorage.getItem("savings"));

/* if ((localStorage.getItem("savings") == NaN) || (localStorage.getItem("needs")) == NaN) || (localStorage.getItem("wants") == NaN)) {
    localStorage.setItem("savings", 0) 
    localStorage.setItem("needs", 0)
    localStorage.setItem("wants", 0)
} */

//localStorage.setItem("savings") = 0

var xValues = ["Savings", "Wants", "Needs"];
var yValues = [
  localStorage.getItem("savings") / localStorage.getItem("total"),
  localStorage.getItem("wants") / localStorage.getItem("total"),
  localStorage.getItem("needs") / localStorage.getItem("total"),
];

var barColors = ["green", "red", "orange"];

try {
  new Chart("donutChart", {
    type: "doughnut",
    data: {
      labels: xValues,
      datasets: [
        {
          backgroundColor: barColors,
          data: yValues,
        },
      ],
    },
    options: {
      tooltips: {
        enabled: false,
      },
      title: {
        display: true,
        text: "Spending Distribution",
        fontSize: 30,
      },
      plugins: {
        legend: {
          display: false,
        },
        datalabels: {
          formatter: (value, ctx) => {
            let datasets = ctx.chart.data.datasets;
            if (datasets.indexOf(ctx.dataset) === datasets.length - 1) {
              let sum = datasets[0].data.reduce((a, b) => a + b, 0);
              let percentage = Math.round((value / sum) * 100) + "%";
              return percentage;
            } else {
              return percentage;
            }
          },
          color: "#FFF",
          fontSize: 20,
        },
      },
    },
  });
} catch (error) {
  console.log(error);
}

/* const config = {
  type: "pie",
  options: {
    plugins: {
      datalabels: {
        render: "value",
        fontColor: ["red", "red", "red"],
      },
    },
  },
}; */

try {
  let savings = parseFloat(document.getElementById("savings").innerText);
  let needs = parseFloat(document.getElementById("needs").innerText);
  let wants = parseFloat(document.getElementById("wants").innerText);

  console.log(savings);
  console.log(needs);
  console.log(wants);
  console.log(savings + needs + wants);

  let total = savings + needs + wants;

  localStorage.setItem("savings", savings);
  localStorage.setItem("needs", needs);
  localStorage.setItem("wants", wants);
  localStorage.setItem("total", total);
} catch (error) {
  console.log(error);
}

var xValues = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12];
var yValues = [7, 8, 8, 9, 9, 9, 10, 11, 14, 14, 15, 0];

try {
  localStorage.setItem("January", 0),
    localStorage.setItem("February", 0),
    localStorage.setItem("March", 0),
    localStorage.setItem("April", 0),
    localStorage.setItem("May", 0),
    localStorage.setItem("June", 0),
    localStorage.setItem("July", 0),
    localStorage.setItem("August", 0),
    localStorage.setItem("September", 0),
    localStorage.setItem("October", 0),
    localStorage.setItem("November", 0),
    localStorage.setItem("December", 0);

  months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
  ];

  month = document.getElementById("month").innerText;
  month = parseInt(month);
  console.log(localStorage.getItem("total"));
  console.log(month);
  yValues[month] = localStorage.getItem("total");

  yValues.forEach((element, index) => {
    if (index == month - 1) {
      console.log(months[month - 1]);
      currentMonth = months[month - 1];

      localStorage.setItem(currentMonth, localStorage.getItem("total"));

      //console.log(localStorage.getItem(currentMonth));

      yValues[index] = localStorage.getItem(currentMonth);
    } else {
      yValues[index] = localStorage.getItem(months[index]);
    }
  });
} catch (error) {
  console.log(error);
}

console.log(yValues);

try {
  new Chart("lineGraph", {
    type: "line",
    data: {
      labels: xValues,
      datasets: [
        {
          fill: false,
          lineTension: 0,
          backgroundColor: "rgba(0,0,255,1.0)",
          borderColor: "rgba(0,0,255,0.1)",
          data: yValues,
        },
      ],
    },
    options: {
      title: {
        display: true,
        text: "Monthly Spending",
        fontSize: 30,
      },
      legend: { display: false },
      scales: {
        yAxes: [{ ticks: { min: 0 } }],
      },
      plugins: {
        datalabels: {
          display: false,
        },
      },
    },
  });
} catch (error) {
  console.log(error);
}
