const TEMP_MIN = 190;
const TEMP_MAX = 215;
const AQ_MIN = 7;

function checkTmpAndAqLogs(log: string, controller: string) {
  const [templog, aqlog] = log.split("AqLog");
  const temps = parseLog(templog);
  const aqs = parseLog(aqlog);

  const tempErrors = temps.reduce(
    (sum, tmp) => (tmp < TEMP_MIN || tmp > TEMP_MAX ? sum + 1 : sum),
    0
  );
  const aqErrors = aqs.reduce((sum, aq) => (aq < AQ_MIN ? sum + 1 : sum), 0);

  console.log("=== ", controller, " ===");
  console.log("Temeprature errors:", tempErrors);
  console.log("Air Quality errors: ", aqErrors);
  console.log("Total errors: ", tempErrors + aqErrors);
  console.log("----------------------------");
}

function parseLog(str: string | undefined) {
  if (!str) return [];

  return str
    .replaceAll("\n", " ")
    .split(",")
    .map((str) => {
      const [left] = str.split(" ");
      const val = left.replace(")", "");
      return parseInt(val);
    })
    .filter((n) => n > -1_000_000);
}

const meta_log = await Deno.readTextFile("./log_analysis/meta_log.txt");
const eco_log = await Deno.readTextFile("./log_analysis/eco_log.txt");
const comfort_log = await Deno.readTextFile("./log_analysis/comfort_log.txt");

checkTmpAndAqLogs(meta_log, "Meta");
checkTmpAndAqLogs(eco_log, "Eco");
checkTmpAndAqLogs(comfort_log, "Comfort");
