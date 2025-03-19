{
  services = {
    postgres = {
      enable = true;
      listen_addresses = "127.0.0.1";
      port = 5432;
      initialDatabases = [
        {
          name = "litellm";
          user = "james";
          pass = "111111";
        }
      ];
    };
  };
}
