const { execSync } = require('child_process');
const isWin = process.platform === 'win32';
const cmd = isWin
  ? 'cd packages/backend-java && gradlew.bat bootRun -Dserver.port=8081'
  : 'cd packages/backend-java && ./gradlew bootRun -Dserver.port=8081';
execSync(cmd, { stdio: 'inherit', shell: true }); 