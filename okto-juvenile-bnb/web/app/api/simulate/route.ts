import { NextResponse } from 'next/server';
import { exec } from 'child_process';
import path from 'path';

type SimResult = {
  success: boolean;
  output?: string;
  logs?: string[];
  error?: string;
};

function runSimulation(cwd: string): Promise<SimResult> {
  return new Promise((resolve) => {
    exec('python3 ops/grid_live.py --auto-regime', { cwd }, (error, stdout, stderr) => {
      if (error) {
        resolve({
          success: false,
          output: stderr || error.message,
          logs: ['Error executing simulation', error.message],
        });
        return;
      }

      const logs = stdout.split('\n').filter((line) => line.trim() !== '');
      resolve({ success: true, output: stdout, logs });
    });
  });
}

export async function POST(): Promise<Response> {
  try {
    // Determine the root directory of the project
    // Assuming the web app is running from `web/` or the root `okto-juvenile-bnb/`
    // We need to execute the python script from the project root.
    
    // In a typical monorepo setup or this specific structure:
    // project-root/
    //   ops/
    //     grid_live.py
    //   web/
    //     app/
    //       api/
    //         simulate/
    //           route.ts
    
    // We want to run: python3 ops/grid_live.py --auto-regime --dry-run
    // The CWD for the command should be the project root.
    
    const projectRoot = path.resolve(process.cwd(), '..'); // Assuming Next.js runs in 'web' folder
    // If Next.js runs in root, then process.cwd() is projectRoot.
    // Let's try to detect based on existence of 'ops' folder.
    
    let commandCwd = process.cwd();
    let fs = require('fs');
    
    if (!fs.existsSync(path.join(commandCwd, 'ops'))) {
        // If 'ops' not in current dir, maybe we are in 'web', so go up one level
        if (fs.existsSync(path.join(path.resolve(commandCwd, '..'), 'ops'))) {
            commandCwd = path.resolve(commandCwd, '..');
        }
    }
    
    console.log(`Executing simulation in: ${commandCwd}`);

    const result = await runSimulation(commandCwd);
    if (!result.success) {
      return NextResponse.json(result, { status: 500 });
    }
    return NextResponse.json(result);

  } catch (error: any) {
    return NextResponse.json({ 
      success: false, 
      error: error.message 
    }, { status: 500 });
  }
}
