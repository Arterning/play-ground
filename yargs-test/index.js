const fs = require('fs');
const yargs = require('yargs');

/**
 * node index.js add --task="good job" --comment="吃饭"
 */
yargs.command({
  command: 'add',
  describe: 'Add a new task',
  builder: {
    task: {
      describe: 'Task to add',
      demandOption: true,
      type: 'string'
    },
    comment: {
      describe: 'Comment to add',
      type: 'string',
      default: 'No comment'
    }
  },
  handler: function (argv) {
    const task = {
      task: argv.task,
      comment: argv.comment,
      id: Date.now(),
      done: false,
      created: new Date(),
      modified: new Date()
    }
    // if tasks.json is not found, create it
    if (!fs.existsSync('tasks.json')) {
      fs.writeFileSync('tasks.json', '[]');
    }
    const tasks = JSON.parse(fs.readFileSync('tasks.json', 'utf8'));
    //add new task to the head
    tasks.unshift(task);
    fs.writeFileSync('tasks.json', JSON.stringify(tasks));
    console.log('Task added!');
  }
});

//add commands to display all the tasks
yargs.command({
  command: 'list',
  describe: 'List all tasks',
  handler: function () {
    const tasks = JSON.parse(fs.readFileSync('tasks.json', 'utf8'));
    console.table(tasks);
  }
})

//add command to popup the first task
yargs.command({
  command: 'popup',
  describe: 'Popup the first task',
  handler: function () {
    const tasks = JSON.parse(fs.readFileSync('tasks.json', 'utf8'));
    //remove the first task
    tasks.shift();
    //write to files
    fs.writeFileSync('tasks.json', JSON.stringify(tasks));
    console.log(tasks);
  }
})

yargs.parse();