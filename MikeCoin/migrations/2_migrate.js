const MikeCoin = artifacts.require('MikeCoin.sol');

module.exports = function(deployer) {
  deployer.then(async () => {

    await deployer.deploy(MikeCoin);

  });
};
