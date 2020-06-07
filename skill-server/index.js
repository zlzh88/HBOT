const express = require('express');
const app = express();
const logger = require('morgan');
const bodyParser = require('body-parser');

const apiRouter = express.Router();

app.use(logger('dev', {}));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({
  extended: true
}));

app.use('/api', apiRouter);

apiRouter.post('/info_mask', function(req, res) {
  const responseBody = {
    version: "2.0",
    template: {
      outputs: [
        {
          basicCard: {
	    title: "마스크 관련 안내사항"
	    description: ""
	  }
        }
      ]
    }
  };

  res.status(200).send(responseBody);
});


app.listen(12345, function() {
  console.log('발문 대기중');
});
