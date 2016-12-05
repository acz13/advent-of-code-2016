require 'digest/md5'

start_time = Time.now

id = ARGV[0]
printf "Solving %s\n", id
pass1 = ''
pass2 = [nil] * 8
index = 0
md5 = Digest::MD5.new

while pass2.include?(nil)
  hash = md5.hexdigest(id + index.to_s)
  if hash.start_with?('00000')
    printf("%s %s\n", hash, index.to_s)
    if pass1.length < 8
      pass1 += hash[5]
      if pass1.length == 8
        printf "Found part 1 in %.2f seconds: %s\n", Time.now-start_time, pass1
      end
    end
    pos = hash[5].to_i(16)
    if pos < 8 and not pass2[pos]
      pass2[pos] = hash[6]
    end
  end
  index += 1
  # Print every 10,000th hash in a cool animation
  if index % 10000 == 0
    printf("%s %s\r", hash, index.to_s)
  end
end

printf "Found part 2 in %.2f seconds: %s\n", Time.now-start_time, pass2.join()
