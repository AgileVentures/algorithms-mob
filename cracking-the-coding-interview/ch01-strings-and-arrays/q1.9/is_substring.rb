class String
    def rotated?(other)
        return false if other.length != length
        # waterbottle <- self
        # terbottlewa <- other
        # 'terbottlewaterbottlewa'.include?("waterbottle")
        (other*2).include?(self)
    end
end
